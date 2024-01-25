#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        # Create an instance of the Redis client and flush the Redis database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        random_key = str(uuid.uuid4())

        # Store the input data in Redis using the random key
        self._redis.set(random_key, data)

        # Return the generated key
        return random_key

    def get(self, key: str, fn=None):
        # Retrieve data from Redis associated with the key
        data = self._redis.get(key)

        # If data exists, apply the conversion function if provided and return
        return fn(data) if fn is not None else data

    def get_str(self, key: str):
        # Shortcut method to get data as a decoded UTF-8 string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        # Shortcut method to get data as an integer
        return self.get(key, fn=int)
