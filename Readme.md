# 🗺️ ItineraryEngine

ItineraryEngine is a robust backend system developed using FastAPI that allows users to generate and manage travel itineraries based on user preferences. It exposes RESTful APIs to interact with trip data, optimize travel plans, and store information in a structured database.

# ⚙️ Features
- Create and retrieve personalized travel itineraries.
- REST API built with FastAPI.
- Database support with SQLAlchemy.
- Auto-reload and interactive documentation using Swagger UI.
- Input validation using Pydantic.
- Easy integration for future authentication/authorization.

# Dependencies
- Main packages used:
  -  fastapi
  -  uvicorn
  -  sqlalchemy
  -  pydantic
  -  python-dotenv
 
# 🔧 Setup Instructions
- Clone the Repository
  ```git clone https://github.com/Rishav123raj/ItineraryEngine.git```
  ```cd ItineraryEngine```
- Create Virtual Environment
  ```python -m venv venv```
  ```source venv/bin/activate```  # on Linux/Mac
  ```venv\Scripts\activate```     # on Windows
- Install Dependencies
- Set Up Environment Variables
    - Create a .env file in the root directory : ```DATABASE_URL=sqlite:///./itineraries.db```
- Run the app
