#!/usr/bin/env python3
"""This script will deal with average score of students"""
import pymongo


def top_students(mongo_collection):
    """This function will return the average scores of students"""
    for student in mongo_collection.find():
        total = 0
        for subject in student["topics"]:
            total += subject["score"]
        ave = total / 3
        mongo_collection.update_one({"name": student["name"]},
                                    {'$set': {"averageScore": ave}})
    return mongo_collection.find().sort("averageScore", pymongo.DESCENDING)
