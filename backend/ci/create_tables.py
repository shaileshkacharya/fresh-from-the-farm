import os
import asyncio
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine

# Import models so SQLModel metadata is populated
# Adjust imports to include any modules that define SQLModel models
try:
    from app.models import user  # noqa: F401
except ImportError:
    pass


def get_database_url():
    return os.environ.get("DATABASE_URL")


async def create_tables():
    database_url = get_database_url()
    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable is not set")
    engine = create_async_engine(database_url, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(create_tables())
