# watchAll – Movie Catalogue API (FastAPI)

**watchAll** is a simple RESTful Movie Catalogue API built with FastAPI.  
It demonstrates basic CRUD operations using an in-memory list (`MOVIES`) as a mock database.

---

## Features

- List all movies or filter by **genre** or **director**
- Retrieve a single movie by **ID**
- Add new movies
- Update movies (full or partial)
- Delete movies and automatically reindex IDs
- Case-insensitive search
- Swagger UI and ReDoc for testing

---

## Tech Stack

- **Python 3.13+**
- **FastAPI**
- **Uvicorn** (for local server)

---

## Setup & Installation

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Run the API
uvicorn main:app --reload
📚 Available Endpoints
Method	Endpoint	Description
GET	/api/v1/movies	Get all movies or filter by ?genre= and/or ?director=
GET	/api/v1/movies/{movie_id}	Get movie by ID
POST	/api/v1/movies	Add a new movie
PUT	/api/v1/movies/{movie_id}	Replace an existing movie (full update)
PATCH	/api/v1/movies/{movie_id}	Partially update a movie
DELETE	/api/v1/movies/{movie_id}	Delete a movie and reindex IDs

Testing via Swagger
After starting the app, open your browser at:
http://localhost:8000/docs

Run these example tests:

GET /api/v1/movies → returns all 5 movies
GET /api/v1/movies?genre=Math → returns []
GET /api/v1/movies?genre=Action → returns Desert Run
GET /api/v1/movies/2 → returns Desert Run
GET /api/v1/movies/99 → { "detail": "Movie not found" }
POST /api/v1/movies → adds new film with id = len(MOVIES)
PUT /api/v1/movies/1 → replaces movie at index 1
PATCH /api/v1/movies/0 → partially updates only specified fields
DELETE /api/v1/movies/3 → removes movie, reindexes IDs 0..n-1

Notes

This project uses an in-memory list as a mock database.
All data is lost when the server restarts.
Future versions could use SQLite or MongoDB for persistence.

Example Run
INFO:     Will watch for changes in these directories: ['.']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Visit:
Swagger UI → http://localhost:8000/docs
ReDoc → http://localhost:8000/redoc

Author: Ebrima Gajaga
Built with ❤️ using FastAPI.
```
