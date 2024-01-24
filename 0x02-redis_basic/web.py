#!/usr/bin/env python3
"""The web cache module"""

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """The cache decorator to store function results in Redis"""

    @wraps(fn)
    def wrapper(url):
        """The wrapper for decorator"""
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """This fetches HTML content of given URL and caches the result
    """
    response = requests.get(url)
    return response.text
