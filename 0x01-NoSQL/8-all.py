#!/usr/bin/env python3
""" List all document in the given MongoDB collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Arguments:
    mongo_collection: pymongo collection object

    Returns: List of documents in the collection
    """
    # Initializze an empty list to store the documents
    all_documents = []

    # Use find() method to retrieve all documents from the collectio
    cursor = mongo_collection.find()

    # Check if cursor is None (indicating no documents found)
    if cursor is  not None:
        # Iterate over the cursor to extract each element
        for document in cursor:
            # Append each document to the list
            all_documents.append(document)

    return all_documents
