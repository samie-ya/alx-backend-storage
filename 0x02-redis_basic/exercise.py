#!/usr/bin/env python3
"""This script will create a class to run redis"""
import redis
import uuid
from typing import Union


class Cache():
    """This class will create a connection to redis"""
    def __init__(self):
        """This function will intialize a class"""
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        """This function will take an argument and return a string"""
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
