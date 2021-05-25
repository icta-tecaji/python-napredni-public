from typing import Dict

from app.crud.auth import get_current_user, get_password_hash
from app.db import database, users
from app.schemas.user import User, UserCreate
from fastapi import Depends, HTTPException


async def get_user_by_email(email: str):
    query = users.select().where(email == users.c.email)
    return await database.fetch_one(query=query)


async def get_user_by_username(username: str):
    query = users.select().where(username == users.c.username)
    return await database.fetch_one(query=query)


async def post_create_user(user: UserCreate) -> Dict:
    password_hash = get_password_hash(user.password)
    query = users.insert().values(
        email=user.email,
        username=user.username,
        hashed_password=password_hash,
        is_active=True,
    )
    await database.execute(query=query)
    created_user = await get_user_by_username(user.username)
    return dict(created_user)


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.get("is_active"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
