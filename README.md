# GitHub Repository Tracker

A FastAPI application that tracks GitHub repositories and stores repository metadata in PostgreSQL.

## Features

- Add GitHub repositories
- Fetch repository metadata from the GitHub API
- Store data in PostgreSQL
- Update repository information
- Delete repositories
- List repositories with pagination
- Custom exception handling

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Pydantic
- HTTPX

## Prerequisites

- Python 3.10+
- PostgreSQL 13+ (running locally or accessible remotely)
- A PostgreSQL database created for this project

## Installation

### 1. Clone the repository

git clone <repository-url>
cd github-repository-tracker

### 2. Create and activate a virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file in the project root:

DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/github_tracker

GITHUB_API_BASE=https://api.github.com

REQUEST_TIMEOUT=30

No GitHub authentication token is required — the app calls the public GitHub API unauthenticated. Note that unauthenticated requests are subject to GitHub's lower rate limit (60 requests/hour per IP), so heavy use may hit that limit.

### 5. Run database migrations (if applicable)

alembic upgrade head

### 6. Run the application

uvicorn app.main:app --reload

The API will be available at http://127.0.0.1:8000.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| POST | /repositories | Add a new repository and fetch its metadata from GitHub |
| GET | /repositories | List tracked repositories (supports pagination) |
| GET | /repositories/{id} | Get a single repository by ID |
| PUT | /repositories/{id} | Update repository information |
| DELETE | /repositories/{id} | Delete a repository |

### Example: Add a repository

curl -X POST http://127.0.0.1:8000/repositories -H "Content-Type: application/json" -d '{"owner": "fastapi", "name": "fastapi"}'

Response:
{
  "id": 1,
  "owner": "fastapi",
  "name": "fastapi",
  "stars": 75000,
  "forks": 6400,
  "language": "Python",
  "created_at": "2026-06-17T10:00:00Z"
}

### Example: List repositories with pagination

curl "http://127.0.0.1:8000/repositories?skip=0&limit=10"

### Error Responses

The API returns structured error responses for invalid input or failures, e.g.:

{
  "detail": "Repository not found"
}

## Documentation

Interactive API documentation (Swagger UI) is available once the app is running:

http://127.0.0.1:8000/docs

Alternative ReDoc documentation:

http://127.0.0.1:8000/redoc

## Testing

No automated test suite yet. Contributions adding pytest coverage are welcome.

## License

This project is licensed under the MIT License.
