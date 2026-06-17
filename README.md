# GitHub Repository Tracker

## Overview

A FastAPI application that tracks GitHub repositories and stores repository metadata in PostgreSQL.

## Features

- Add GitHub repositories
- Fetch repository metadata from GitHub API
- Store data in PostgreSQL
- Update repository information
- Delete repositories
- List repositories
- Pagination support
- Custom exception handling

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy Async
- Pydantic
- HTTPX

## Installation

### Clone Repository

git clone <repository-url>

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/github_tracker

GITHUB_API_BASE=https://api.github.com

REQUEST_TIMEOUT=30

### Run Application

uvicorn app.main:app --reload

## API Endpoints

POST /repositories

GET /repositories

GET /repositories/{id}

PUT /repositories/{id}

DELETE /repositories/{id}

## Documentation

Swagger UI:

http://127.0.0.1:8000/docs