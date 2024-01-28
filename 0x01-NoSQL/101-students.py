#!/usr/bin/env python3
""" function that returns all students sorted by average score """


def top_students(mongo_collection):
    # Use MongoDB's aggregation framework to calculate average scores
    students = mongo_collection.aggregate([
        {
            "$unwind": "$scores"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": { "$first": "$name"},
                "averageScore": {
                    "$avg": "$scores.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1  # Sort in descending order
            }
        }
    ])

    # Convert the result to a list and return it
    return list(students)
