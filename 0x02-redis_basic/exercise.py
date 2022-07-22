#!/usr/bin/env python3
"""This script will create a class to run redis"""
import redis
import uuid
from typing import Union, Optional, Any, Callable
from functools import wraps


class Cache:
    """This class will create a connection to redis server"""
    def __init__(self):
        """This function will intialize a class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This function will take an argument and return a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
