from app.crud.user import (
    get_current_active_user,
    get_user_by_email,
    get_user_by_username,
    post_create_user,
)
from app.schemas.user import User, UserCreate
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.post("/", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    # preverimo ali mail že obstaja
    db_user_email = await get_user_by_email(email=user.email)
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already exists.")
    # preverimo ali username obstaja
    db_user_username = await get_user_by_username(username=user.username)
    if db_user_username:
        raise HTTPException(status_code=400, detail="Username already registered.")
    created_user = await post_create_user(user=user)
    return created_user


@router.get("/me/", response_model=User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user
