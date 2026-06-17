# GitHub Repository Tracker

A FastAPI application that tracks GitHub repositories and stores repository metadata in PostgreSQL.

## Features

- CRUD operations for GitHub repositories
- GitHub API integration
- PostgreSQL persistence
- Async SQLAlchemy
- Pagination support
- Duplicate repository detection
- Custom exception handling
- OpenAPI/Swagger documentation

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

git clone https://github.com/vamshi241010/github-repository-tracker.git

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

## Environment Variables

| Variable | Description |
|-----------|-------------|
| DATABASE_URL | PostgreSQL connection string |
| GITHUB_API_BASE | GitHub API base URL |
| REQUEST_TIMEOUT | HTTP request timeout in seconds |

No GitHub authentication token is required — the app calls the public GitHub API unauthenticated. Note that unauthenticated requests are subject to GitHub's lower rate limit (60 requests/hour per IP), so heavy use may hit that limit.

## Project Structure

app/
├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/

### Architecture

Route Layer
↓
Service Layer
↓
Repository Layer
↓
Database

### 5. Run the application

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

curl -X POST http://127.0.0.1:8000/repositories \
-H "Content-Type: application/json" \
-d '{"url":"https://github.com/fastapi/fastapi"}'

Response:
{
  "id": 1,
  "github_id": 160919119,
  "owner": "fastapi",
  "repo_name": "fastapi",
  "full_name": "fastapi/fastapi",
  "description": "...",
  "stars": 85000,
  "forks": 7000,
  "language": "Python",
  "html_url": "https://github.com/fastapi/fastapi"
}

### Example: List repositories with pagination

curl "http://127.0.0.1:8000/repositories?page=1&size=10"

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
