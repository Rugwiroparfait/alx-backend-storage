#!/usr/bin/env python3
"""
Cache module for interacting with Redis.
"""

import redis
import uuid
from typing import Union


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


if __name__ == "__main__":
    # Example usage
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
