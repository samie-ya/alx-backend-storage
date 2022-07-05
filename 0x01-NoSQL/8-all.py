#!/usr/bin/env python3
"""This script will list all document in a collection"""


def list_all(mongo_collection):
    """This function will return list of all document"""
    lists = mongo_collection.find({})
    if (lists):
        return lists
    return []
