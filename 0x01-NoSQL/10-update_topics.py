#!/usr/bin/env python3
""" A function that update all the topics of a school document. """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Args:
    mongo_collection: pymongo collection object
    name: School name to update
    topics: List of topics to be updated for the school

    Returns:
    None
    """
    # Create a new document with the updated topics
    new_value = {"$set": {"topics": topics}}

    # Update the document in the MongoDB
    mongo_collection.update_one({"name": name}, new_value)
