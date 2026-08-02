# README for backend

This backend provides a FastAPI-based API for Fresh From The Farm.

Quickstart (development):

1. Copy environment variables:

   cp .env.example .env

2. Start with Docker Compose (from backend/):

   docker compose up --build

3. Open docs:

   http://localhost:8000/docs

Notes:
- This branch (feat/package-1b) introduces:
  - Poetry-style pyproject
  - Pydantic Settings
  - Application factory and /api/v1 router
  - Async SQLModel + startup DB create_all (for dev)
  - Alembic skeleton for migrations
  - Simple test and CI workflow

Next steps:
- Add authentication models and endpoints
- Finalize Alembic migration scripts and CI migration checks
- Add more tests and linting config enforcement
