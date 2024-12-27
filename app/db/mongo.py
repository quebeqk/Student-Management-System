import pymongo
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from typing import Optional
from uuid import uuid4

# Load environment variables from the .env file
load_dotenv()

# MongoDB connection URL
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB client instance
client = MongoClient(MONGO_URI)
# Database connection
db = client["student_db"]
# Collection for students data
students_collection = db["students"]

# CRUD Functions

def get_students_collection():
    "Return the students collection."
    return students_collection

def get_student_by_id(student_id: str) -> Optional[dict]:
    "Fetch a student by ID from the database."
    student = students_collection.find_one({"id": student_id})
    if student:
        return {
            "id": str(student["_id"]),
            "name": student["name"],
            "age": student["age"],
            "address": student["address"]
        }
    return None

def create_student(student_data: dict) -> dict:
    "Create a new student record in the database."
    student_data['id'] = str(uuid4())
    students_collection.insert_one(student_data)
    return {"id": student_data["id"]}

def update_student(student_id: str, update_data: dict) -> dict:
    "Update a student's information in the database"
    result = students_collection.update_one({"id": student_id}, {"$set": update_data})
    return {"modified_count": result.modified_count}

def delete_student(student_id: str) -> dict:
    "Delete a student from the database."
    result = students_collection.delete_one({"id": student_id})
    return {"deleted_count": result.deleted_count}