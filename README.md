# Student Management System

## Overview

The **Student Management System** is a backend application built using **FastAPI**. It is designed to manage student records efficiently and integrates with **MongoDB Atlas** for cloud-based database storage. The application is containerized using **Docker**, which ensures scalability and ease of deployment. This API supports CRUD operations for managing student records while adhering to RESTful principles.

---

## Features

- **RESTful API** for managing student records.
- Seamless integration with **MongoDB Atlas** (M0 Free Tier) for database storage.
- Fully **Dockerized** for cross-platform compatibility.
- Adheres to strict API specifications with proper request/response structures and status codes.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **Docker** installed.
- Access to a **MongoDB Atlas cluster** (M0 Free Tier or above).

---

## Getting Started

### Setting Up the Project Locally (Without Docker)

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/quebeqk/Student-Management-System.git
   cd Student-Management-System
   ```

2. **Create and Configure Environment Variables:**

   - Create a `.env` file in the root directory:

     ```bash
     touch .env
     ```

   - Add your MongoDB Atlas connection string to the `.env` file:

     ```
     MONGO_URI=<your-mongodb-atlas-connection-uri>
     ```

     Replace `<your-mongodb-atlas-connection-uri>` with your MongoDB Atlas connection string.

3. **Running the Application Locally**

   - **Create and Activate a Virtual Environment**

     For Linux/Mac:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

     For Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - **Install Dependencies**

     ```bash
     pip install -r requirements.txt
     ```

   - **Install Uvicorn** (if not included in `requirements.txt`):

     ```bash
     pip install uvicorn
     ```

   - **Start the Application**

     ```bash
     uvicorn app.main:app --host 0.0.0.0 --port 8000
     ```

     - Access the Application:

       - Open your browser or API client and navigate to `http://localhost:8000`.
       - Access the interactive API documentation at `http://localhost:8000/docs`.

4. **Running the Application with Docker**

   - Stop the Virtual Environment (if Active):

     ```bash
     deactivate  # For Linux/Mac/Windows
     ```

   - **Build the Docker Image**

     ```bash
     docker build -t student-management-system .
     ```

   - **Run the Docker Container**

     ```bash
     docker run --env-file .env -p 8000:8000 student-management-system
     ```

   - Access the Application:

     - Open your browser or API client and navigate to `http://localhost:8000`.
     - Access the interactive API documentation at `http://localhost:8000/docs`.

---

## API Documentation

### API Endpoints and CURL Commands

1. **Create a New Student**  
   **Endpoint:** `POST /students`

   **Request Body:**

   ```json
   {
     "name": "John Doe",
     "age": 20,
     "address": {
       "country": "USA",
       "city": "New York"
     }
   }
   ```

   **CURL Command:**

   ```bash
   curl -X POST "http://localhost:8000/students"    -H "accept: application/json"    -H "Content-Type: application/json"    -d '{
     "name": "John Doe",
     "age": 20,
     "address": {
       "country": "USA",
       "city": "New York"
     }
   }'
   ```

2. **Get All Students (Optional Filters)**  
   **Endpoint:** `GET /students`

   **Query Parameters:**

   - `country` (optional): Filter by country.
   - `age` (optional): Filter by age.

   **CURL Commands:**

   Without Filters:

   ```bash
   curl -X GET "http://localhost:8000/students" -H "accept: application/json"
   ```

   With Filters:

   ```bash
   curl -X GET "http://localhost:8000/students?country=USA&age=20" -H "accept: application/json"
   ```

3. **Get a Student by ID**  
   **Endpoint:** `GET /students/{id}`

   **CURL Command:**

   ```bash
   curl -X GET "http://localhost:8000/students/<id>" -H "accept: application/json"
   ```

4. **Update a Student**  
   **Endpoint:** `PATCH /students/{id}`

   **Request Body (Partial Update):**

   ```json
   {
     "name": "Jane Doe",
     "age": 21
   }
   ```

   **CURL Command:**

   ```bash
   curl -X PATCH "http://localhost:8000/students/<id>"    -H "accept: application/json"    -H "Content-Type: application/json"    -d '{
     "name": "Jane Doe",
     "age": 21
   }'
   ```

5. **Delete a Student**  
   **Endpoint:** `DELETE /students/{id}`

   **CURL Command:**

   ```bash
   curl -X DELETE "http://localhost:8000/students/<id>" -H "accept: application/json"
   ```
