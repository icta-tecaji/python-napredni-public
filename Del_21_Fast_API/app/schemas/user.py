from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str = Field(
        ...,
        title="User email.",
        description="The login email.",
        example="test@example.com",
    )
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_date: datetime
