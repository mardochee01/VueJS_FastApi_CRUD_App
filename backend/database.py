from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["studentdb"]
student_collection = db["students"]