# PR: feat(auth): add JWT auth, RBAC, and CI linting

This PR adds authentication and authorization to the backend and hardens CI to run linting and formatting checks.

Summary of changes

- Add User model with hashed_password, role, and created_at
- Security core (argon2 password hashing, JWT create/verify helpers)
- Auth schemas and dependency helpers (get_current_user, role_required)
- Auth router with endpoints:
  - POST /api/v1/auth/register
  - POST /api/v1/auth/token
  - POST /api/v1/auth/refresh
  - GET /api/v1/auth/me
- Unit tests (in-memory SQLite) for register/login flows
- CI: run ruff, black --check, and pytest in GitHub Actions
- .env.example updated with JWT settings

How to test locally (backend/)

1. cp .env.example .env (fill JWT_SECRET)
2. Run unit tests: pytest -q
3. Start app: docker compose up --build (or run uvicorn for local dev)
4. Register and login via /api/v1/auth endpoints

Checklist

- [ ] Tests pass locally (pytest)
- [ ] Linting and formatting run (ruff/black)
- [ ] CI is passing on GH Actions
- [ ] Confirm no secrets in .env or committed files

PR base: feat/package-1b
PR head: feat/auth

This PR is ready for review.
