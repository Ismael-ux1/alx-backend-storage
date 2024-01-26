#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import time
from functools import lru_cache


def cache_with_expiration(seconds: int):
    # Define a decorator to cache the result with expiration time
    def wrapper_cache(func):
        func = lru_cache(maxsize=None)(func)
        func.expiration = {}

        def wrapped_func(url):
            if url in func.expiration and time.time() < func.expiration[url]:
                return func(url)
            else:
                result = func(url)
                func.expiration[url] = time.time() + seconds
                return result

        return wrapped_func

    return wrapper_cache


def get_page(url: str) -> str:
    # Use requests to get the HTML content with a timeout
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

    if response.status_code == 200:
        # Increment the count for the url
        key = f"count:{url}"
        count = int(requests.get(key).text) if requests.get(key).text else 0
        requests.post(key, data={"count": count + 1})
        return response.text
    else:
        return ""
