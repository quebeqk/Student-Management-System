from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from db import create_student, get_students_collection, get_student_by_id, update_student, delete_student

# FastAPI app initialization
app = FastAPI()

# Pydantic Models
class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(BaseModel):
    id: str

class StudentDetails(BaseModel):
    name: str
    age: int
    address: Address

# POST /students - Create a new student
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student_endpoint(student: Student):
    student_data = student.model_dump() 
    created_student = create_student(student_data)
    return {"id": created_student["id"]}  

# GET /students - Fetch all students with optional filters
@app.get("/students", response_model=dict)
def list_students(country: Optional[str] = None, age: Optional[int] = None):
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}

    students_cursor = get_students_collection().find(query)  # Fetch students based on query
    
    response = []
    for student in students_cursor:
        student_data = {
            "name": student["name"],
            "age": student["age"],
            # "country": student.get("address", {}).get("country", ""),
        }
        response.append(student_data)
    return {"data": response}  # Return students in the expected format

# GET /students/{id} - Fetch a student by ID
@app.get("/students/{id}", response_model=StudentDetails, status_code=200)
def get_student_endpoint(id: str):
    student = get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# PATCH /students/{id} - Update student details
@app.patch("/students/{id}", status_code=204)
def update_student_endpoint(id: str, update_data: Student):
    updated_student = update_student(id, update_data.model_dump(exclude_unset=True))
    if updated_student["modified_count"] == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return # 204 No Content response 

# DELETE /students/{id} - Delete a student
@app.delete("/students/{id}", status_code=200)
def delete_student_endpoint(id: str):
    result = delete_student(id)
    if result["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": f"Student {id} deleted successfully"}