#!/usr/bin/env python3
"""This script will create a class to run redis"""
import redis
import uuid
from typing import Union, Optional, Any


class Cache:
    """This class will create a connection to redis"""
    def __init__(self):
        """This function will intialize a class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """This function will take an argument and return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Any]):
        """This function will convert a data back to its original type"""
        if (callable(fn)):
            return fn(self._redis.get(key))
        return self._redis.get(key)
