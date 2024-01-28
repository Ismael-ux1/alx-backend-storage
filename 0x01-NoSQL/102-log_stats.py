#!/usr/bin/env python3
""" A script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

# Establish a connection to the MongoDB instance
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client['logs']
collection = db['nginx']

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of each method type
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({
                 "method": method}) for method in methods}

# Count the number of 'status check' documents
status_check_count = collection.count_documents({"method": "GET",
                                                 "path": "/status"})

# Get the top 10 most present IPs
top_ips = collection.aggregate([
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

# Print the total number of logs
print(f"{total_logs} logs")

# Print the count of each HTTP method type
print("Methods:")
for method, count in method_counts.items():
    print(f"    method {method}: {count}")

# Print the count of 'status check' documents
print(f"{status_check_count} status check")

# Print the top 10 most present IPs
print("IPs:")
for ip in top_ips:
    print(f"    IP {ip['_id']}: {ip['count']}")
