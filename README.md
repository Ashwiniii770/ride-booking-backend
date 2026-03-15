# Ride Booking Backend API

## Overview
This project is a backend system for a **Ride Booking Application** built using **FastAPI** and **SQLite**.  
It provides REST API endpoints to manage riders, drivers, and ride bookings.
 
## Features
- Rider registration and management
- Driver registration and management
- Ride booking system
- Database integration with SQLite
- REST API using FastAPI

## Tech Stack
- Python
- FastAPI
- SQLite
- REST API

## Project Structure
ride-booking-backend/
│
├── main.py        # FastAPI application entry point
├── database.py    # Database connection
├── models.py      # Data models
├── db_models.py   # Database schema
├── riders.py      # Rider APIs
├── drivers.py     # Driver APIs
├── rides.db       # SQLite database
└── README.md

## Running the Project

Install dependencies:


## API Endpoints

POST /riders
POST /drivers
POST /rides
GET /rides




## How to Run the Project

### 1. Clone the Repository

Download the project from GitHub:

```
git clone https://github.com/Ashwiniii770/ride-booking-backend.git
```

### 2. Navigate to the Project Folder

```
cd ride-booking-backend
```

### 3. Install Required Dependencies

```
pip install fastapi uvicorn
```

### 4. Run the FastAPI Server

```
uvicorn main:app --reload
```

### 5. Open API Documentation

Open the browser and go to:

```
http://127.0.0.1:8000/docs
```

This will open **Swagger UI**, where you can test all API endpoints.

