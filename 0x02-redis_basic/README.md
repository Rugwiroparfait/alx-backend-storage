# Redis Basic Project


## Learning Objectives

By the end of this project, you should be able to:
1. Use Redis for basic operations.
2. Utilize Redis as a simple cache.

## Requirements

- All files must be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- A `README.md` file must be present at the root of the project folder.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All modules, classes, and functions must be documented.
- Functions and coroutines must include type annotations.

## Tasks

### Task 0: Writing Strings to Redis

Create a `Cache` class with the following requirements:
- **`__init__` Method:** Initializes a Redis client instance and flushes the database.
- **`store` Method:** Stores data in Redis with a random key and returns the key.

Example:
```python
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

Repository:
- **GitHub Repository:** [alx-backend-storage](https://github.com/your-repo/alx-backend-storage)
- **Directory:** `0x02-redis_basic`
- **File:** `exercise.py`

### Task 1: Reading from Redis and Recovering Original Type

Enhance the `Cache` class with:
- **`get` Method:** Retrieves data and uses an optional callable to convert it back to the desired format.
- **`get_str` and `get_int` Methods:** Automatically use `Cache.get` with appropriate conversion functions.

Repository:
- **GitHub Repository:** [alx-backend-storage](https://github.com/your-repo/alx-backend-storage)
- **Directory:** `0x02-redis_basic`
- **File:** `exercise.py`

### Task 2: Incrementing Values

Implement a decorator `count_calls` that tracks method calls:
- **`count_calls` Decorator:** Increments a counter in Redis each time a method is called.
- Decorate `Cache.store` with `count_calls`.

Example:
```python
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

Repository:
- **GitHub Repository:** [alx-backend-storage](https://github.com/your-repo/alx-backend-storage)
- **Directory:** `0x02-redis_basic`
- **File:** `exercise.py`

### Task 3: Storing Lists

Create a `call_history` decorator to:
- Store input parameters and outputs in Redis lists.
- Decorate `Cache.store` with `call_history`.

Example:
```python
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

Repository:
- **GitHub Repository:** [alx-backend-storage](https://github.com/your-repo/alx-backend-storage)
- **Directory:** `0x02-redis_basic`
- **File:** `exercise.py`

### Task 4: Retrieving Lists

Implement a `replay` function to display the history of function calls:
- Use Redis lists to generate a detailed call history.

Example:
```python
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> <uuid>
Cache.store(*('bar',)) -> <uuid>
Cache.store(*(42,)) -> <uuid>
```

Repository:
- **GitHub Repository:** [alx-backend-storage](https://github.com/your-repo/alx-backend-storage)
- **Directory:** `0x02-redis_basic`
- **File:** `exercise.py`

---

ALXafrica@2024