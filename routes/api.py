from fastapi import APIRouter
from src.endpoints import roluser

router = APIRouter()

router.include_router(roluser.router)