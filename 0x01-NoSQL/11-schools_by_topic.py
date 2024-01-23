#!/usr/bin/env python3
"""This is a Python function that returns the list
of school having a specific"""


def schools_by_topic(mongo_collection, topic):
    """This returns the list of school having a specific topic"""
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
