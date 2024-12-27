# app/main.py
from fastapi import FastAPI
from .routes.student_routes import router as student_router

app = FastAPI(
    title="Student Management System",
    description="A simple API for managing student data with CRUD operations.",
    version="1.0.0"
)

# Include the student routes from the routes module
app.include_router(student_router)
