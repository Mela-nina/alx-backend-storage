#!/usr/bin/env python3
"""This is a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """This is the list all documents in Python"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
