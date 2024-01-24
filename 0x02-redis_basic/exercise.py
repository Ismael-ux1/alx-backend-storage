#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        # Create an instance of the Redis client and fluch the Redis database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        random_key = str(uuid.uuid4())

        # Store the input data in Redis using the random key
        self._redis.set(random_key, data)

        # Return the generated key
        return random_key
