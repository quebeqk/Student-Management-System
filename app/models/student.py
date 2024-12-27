# app/models/student.py
from pydantic import BaseModel
from typing import Optional

# Address Model
class Address(BaseModel):
    city: str
    country: str

# Student Model (used for input validation)
class Student(BaseModel):
    name: str
    age: int
    address: Address

# Student Response Model (used for response output)
class StudentResponse(BaseModel):
    id: str

# Detailed Student Info (for response)
class StudentDetails(BaseModel):
    name: str
    age: int
    address: Address

#New PartialAddress model for partial update
class PartialAddress(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

# New PartialStudent model for partial updates
class PartialStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[PartialAddress] = None  # Address can also be updated partially if needed