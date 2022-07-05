#!/usr/bin/env python3
"""This script will deal with the logs from nginx"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    total = nginx.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(total))
    print("Methods:")
    for meth in methods:
        value = nginx.find({"method": meth})
        count = 0
        for i in value:
            count += 1
        print("    method {}: {}".format(meth, count))
    path = nginx.find({"path": "/status"}, {"method": "GET"})
    count = 0
    for i in path:
        count += 1
    print("{} status check".format(count))
