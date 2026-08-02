from fastapi import APIRouter

from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Application root")
async def root():
    return {"application": "Fresh From The Farm", "status": "running"}

@router.get("/health", summary="Health check")
async def health():
    return {"status": "healthy"}
