#!/usr/bin/env python3
""" Retrieves a list of schools from a MongoDB collection """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Arguments:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection.
    topic (str): The topic to search for.

    Returns:
    list[str]: The list of school names that have the specified topic.
    """
    # Query the mongodb collection for documents.
    schools = mongo_collection.find({"topics": topic})

    # Return the list of matching documents
    return list(schools)
