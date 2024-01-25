#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
import functools
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    # Decorator to count the number of times a method is called
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the count for the method in Redis
        self._redis.incr(method.__qualname__)

        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    # Decorator to store the history of inputs and outputs for a method
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Normalize the input arguments and store them in Redis
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))

        # Call the original method and store its output in Redis
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", str(output))

        # Return the output
        return output

    return wrapper


class Cache:
    def __init__(self):
        # Create an instance of the Redis client and flush the Redis database
        self._redis = redis.Redis()
        self._redis.flushdb()

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

        # If data exists, apply the conversion function if provided and return
        return fn(data) if fn is not None else data

    def get_str(self, key: str):
        # Shortcut method to get data as a decoded UTF-8 string
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        # Shortcut method to get data as an integer
        return self.get(key, fn=int)

    def replay(self, method: Callable):
        """Method to display the history of calls of a particular method"""
        # Retrieve the input and output history from Redis
        inputs = self._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)

        # Print the history of calls
        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for i, (input_, output) in enumerate(zip(inputs, outputs)):
            print(f"{method.__qualname__}(*{input_}) -> {output}")
