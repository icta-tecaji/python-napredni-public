from fastapi import APIRouter
from app.api.endpoints import ping, user, auth

api_router = APIRouter()

api_router.include_router(ping.router, tags=["Test"])
api_router.include_router(user.router, tags=["User"], prefix="/user")
api_router.include_router(auth.router, tags=["Auth"], prefix="/auth")
