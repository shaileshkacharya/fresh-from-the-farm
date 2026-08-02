Summary of changes

- Switch to Poetry for dependency management (pyproject updated)
- Application factory and /api/v1 router
- Pydantic Settings and structured JSON logging
- Async SQLModel setup + startup DB init and Alembic skeleton
- Fixed Dockerfile and entrypoint (wait-for-postgres)
- Basic tests and CI workflow
- Pre-commit config (ruff, black)

How to run (from backend/)

1. cp .env.example .env
2. docker compose up --build
3. Open http://localhost:8000/docs

Notes / TODO

- Finalize Alembic migrations and remove create_all from startup for production
- Add authentication and authorization in next package
- Expand tests and enforce linting in CI

Checklist

- [ ] Tests pass locally (pytest)
- [ ] Linting and formatting run (ruff/black)
- [ ] CI is passing on GH Actions
- [ ] Confirm no secrets in .env or committed files
- [ ] Remove create_all from startup before production deploy (tracked TODO)
