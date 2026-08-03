from fastapi import APIRouter
from .endpoints import health
from . import auth

api_router = APIRouter()
api_router.include_router(health.router, prefix="", tags=["health"])
api_router.include_router(auth.router, prefix="", tags=["auth"])
