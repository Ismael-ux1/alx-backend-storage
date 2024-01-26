#!/usr/bin/env python3
""" A function that insert a new document in a collection based on kwargs """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Args:
    mongo_collection: pymongo collection object
    kwargs: Keyword arguments representing the fields and,
            values of the new document

    Returns: The new _id of the inserted document
    """
    # Insert the document into the collection and retrive the _id
    result = mongo_collection.insert_one(kwargs)

    # Return the _id of the inserted document
    return result.inserted_id
