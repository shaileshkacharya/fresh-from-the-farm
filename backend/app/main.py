from fastapi import FastAPI
from app.core.settings import settings
from app.core.logging import configure_logging
from app.api.v1.router import api_router
from app.db.session import init_db

app: FastAPI

def create_app() -> FastAPI:
    configure_logging()

    app = FastAPI(title=settings.app_name, version="1.0.0")
    app.include_router(api_router, prefix="/api/v1")

    @app.on_event("startup")
    async def on_startup():
        # initialize DB (create tables for dev). In prod use migrations.
        await init_db()

    return app

# Provide WSGI/ASGI entrypoint
app = create_app()
