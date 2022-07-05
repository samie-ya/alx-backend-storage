#!/usr/bin/env python3
"""This script will deal with update in pymongo"""


def update_topics(mongo_collection, name, topics):
    """This function will update an existing document"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
