from fastapi import APIRouter, HTTPException
from typing import Optional
from app.models.student import Student, StudentDetails, StudentResponse, PartialStudent
from app.db.mongo import create_student, get_students_collection, get_student_by_id, update_student, delete_student

router = APIRouter()

# POST /students - Create a new student
@router.post("/students", response_model=StudentResponse, status_code=201)
def create_student_endpoint(student: Student):
    student_data = student.model_dump() 
    created_student = create_student(student_data)
    return {"id": created_student["id"]}  

# GET /students - Fetch all students with optional filters
@router.get("/students", response_model=dict)
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
            "id": student["id"],
            "name": student["name"],
            "age": student["age"],
            "address": {
                "country": student.get("address", {}).get("country", ""),
                "city": student.get("address", {}).get("city", ""),
            }
        }
        response.append(student_data)
    return {"data": response}  # Return students in the expected format

# GET /students/{id} - Fetch a student by ID
@router.get("/students/{id}", response_model=StudentDetails, status_code=200)
def get_student_endpoint(id: str):
    student = get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# PATCH /students/{id} - Update student details
@router.patch("/students/{id}", status_code=204)
def update_student_endpoint(id: str, update_data: PartialStudent):
    updated_data = update_data.model_dump(exclude_unset=True)
    if not updated_data:
        raise HTTPException(status_code=400, detail="No data provided for update")
    result = update_student(id, updated_data)
    if result["modified_count"] == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return # 204 No Content response 

# DELETE /students/{id} - Delete a student
@router.delete("/students/{id}", status_code=200)
def delete_student_endpoint(id: str):
    result = delete_student(id)
    if result["deleted_count"] == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": f"Student {id} deleted successfully"}