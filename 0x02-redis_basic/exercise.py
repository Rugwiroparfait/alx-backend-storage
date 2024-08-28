#!/usr/bin/env python3
"""
Cache module for interacting with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """
        Initialize the Cache class.

        Store an instance of the Redis client as a private variable
        named _redis and flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    # Example usage of get_str and get_int
    str_key = cache.store("hello")
    int_key = cache.store(42)

    assert cache.get_str(str_key) == "hello"
    assert cache.get_int(int_key) == 42
