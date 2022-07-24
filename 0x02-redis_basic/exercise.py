#!/usr/bin/env python3
"""This script will create a class to run redis"""
import redis
import uuid
from typing import Union, Optional, Any, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """This funtion will be a decorator function to count
       how many times a function has been called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """This function will increament everytime a method is called"""
        key = method.__qualname__
        self._redis.incr(key)
        return method
    return wrapper


class Cache:
    """This class will create a connection to redis server"""
    def __init__(self):
        """This function will intialize a class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This function will take an argument and return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """This function will convert a data back to its original type"""
        if (callable(fn)) and (self._redis.get(key) is not None):
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key):
        """This function will create a conversion function str"""
        return Cache.get(key, str)

    def get_int(self, key):
        """This function will create a conversion function int"""
        return Cache.get(key, int)
