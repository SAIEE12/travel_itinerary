markdown
# Travel Itinerary Management System

A FastAPI-based backend system for creating and managing travel itineraries with recommendation capabilities.

## Key Features

- **Database Models**: Hotels, transfers, activities with relationships
- **REST API**: Create and view itineraries
- **Recommendations**: Get suggested itineraries by duration (2-8 nights)
- **Pre-loaded Data**: Sample data for Phuket and Krabi regions

## Quick Start

 1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

 2.  Set up database:
   ``` bash
   python3 scripts/seed_database.py
   ```
3.  Run the server:
   ```bash

    uvicorn app.main:app --reload
   ```
4.  Access API docs:
   ```bash
    http://localhost:8000/docs
  ```
