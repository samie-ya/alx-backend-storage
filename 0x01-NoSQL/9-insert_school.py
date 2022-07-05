#!/usr/bin/env python3
"""This script will deal with insertion in pymongo"""


def insert_school(mongo_collection, **kwargs):
    """This function will insert new document into collection"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
