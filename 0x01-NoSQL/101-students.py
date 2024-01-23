#!/usr/bin/env python3
"""This is a Python function that returns all students
sorted by average score"""


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """This returns all students sorted by average score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
