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
    True if update is successful, False otherwise
    """
    try:
        # Use a query to find the document with the specified school name
        query = {"name": name}

        # Update the 'topics' field with the provided list of topic
        update = {"$set": {"topics": topics}}

        # Use the update_one method to perform the update
        result = mongo_collection.update_one(query, update)

        # Check if the document was found and update
        if result.matched_count > 0:
            return True
        else:
            print(f"No school with the name '{name}' found.")
            return False

    except Exception as e:
        print(f"Error updating topics: {e}")
        return False
