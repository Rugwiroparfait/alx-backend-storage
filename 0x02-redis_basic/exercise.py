#!/usr/bin/env python3
"""
Cache module with a count_calls decorator to track method calls.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


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

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))  # Output: b'1'

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))  # Output: b'3'
