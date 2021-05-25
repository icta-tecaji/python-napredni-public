from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}
