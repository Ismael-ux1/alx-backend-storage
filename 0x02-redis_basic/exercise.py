#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
import functools
from typing import Union


class Cache:
    def __init__(self):
        # Create an instance of the Redis client and fluch the Redis database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def call_history(method):
        # Define the decorator call_history that takes a method as an argument

        # Use 'functools.wraps' to preserve the original function's
        # metadata when it's decorated
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Use the __qualname__ attribute as the key
            key_inputs = method.__qualname__ + ":inputs"
            key_outputs = method.__qualname__ + ":outputs"

            # Normalize the arguments and use RPUSH to append them
            # to the inputs list in Redis
            self._redis.rpush(key_inputs, str(args))

            # Call the original method and get its output
            output = method(self, *args, **kwargs)

            # Use RPUSH to append the output to the outputs list in Redis
            self._redis.rpush(key_outputs, str(output))

            # Return the output of the original method
            return output

        return wrapper

    def count_calls(method):
        # Use functools.wraps to preserve the original function's metadata
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            # Use qualified name of the method as the key
            key = method.__qualname__

            # Increment count in Redis
            self._redis.incr(key)

            # Call the original method and return its result
            return method(self, *args, **kwargs)
        # Return the decorated function
        return wrapper

    def replay(self, method):
        # Use the __qualname__ attribute as the key
        key_inputs = method.__qualname__ + ":inputs"
        key_outputs = method.__qualname__ + ":outputs"

        # Get the history of inputs and outputs from Redis
        inputs = self._redis.lrange(key_inputs, 0, -1)
        outputs = self._redis.lrange(key_outputs, 0, -1)

        # Print the history of calls to the method
        for i, o in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{i}) -> {o}")

    @call_history
    @count_calls
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

        # If data exists, apply the conversion function and return
        return fn(data) if fn is not None else data

    def get_str(self, key: str):
        # Shortcut method to get data as a decoded UTF-8 string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        # Shortcut method to get data as an integer
        return self.get(key, fn=int)
