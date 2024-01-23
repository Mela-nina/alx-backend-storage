#!/usr/bin/env python3
"""This is a Python function that inserts a new document in
a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """This inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
