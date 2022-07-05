#!/usr/bin/env python3
"""This script will deal with retrieval"""


def schools_by_topic(mongo_collection, topic):
    """This function will search for a specific topic"""
    return mongo_collection.find({"topics": topic})
