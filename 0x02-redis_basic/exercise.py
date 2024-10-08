#!/usr/bin/env python3
"""
Cache module with a call_history decorator to track method call history.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a particular function.

    Args:
        method (Callable): The method to be wrapped.

    Returns:
        Callable: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the inputs and outputs in Redis.

        Args:
            self: The instance of the Cache class.
            *args: Positional arguments to the method.
            **kwargs: Keyword arguments to the method.

        Returns:
            The result of the original method.
        """
        # Define the keys for inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the input arguments as a string in the inputs list
        self._redis.rpush(input_key, str(args))

        # Call the original method and get its result
        result = method(self, *args, **kwargs)

        # Store the result in the outputs list
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def replay(fn: Callable):
    '''display the history of calls of a particular function.'''
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))
    
def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be wrapped.

    Returns:
        Callable: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count in Redis and calls the original method.

        Args:
            self: The instance of the Cache class.
            *args: Positional arguments to the method.
            **kwargs: Keyword arguments to the method.

        Returns:
            The result of the original method.
        """
        # Use the qualified name of the method as the key
        key = method.__qualname__
        # Increment the count for the method in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Cache class.

        Store an instance of the Redis client as a private variable
        named _redis and flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally convert it using a callable.

        Args:
            key (str): The key to retrieve from Redis.
            fn (Optional[Callable]): A callable to convert the data back to the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The data retrieved from Redis, optionally transformed by fn.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decoded string from Redis by key.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[str]: The data as a UTF-8 decoded string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer from Redis by key.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[int]: The data as an integer.
        """
        return self.get(key, fn=int)
    


if __name__ == "__main__":
    # Example usage
    cache = Cache()

    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("secont")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))
