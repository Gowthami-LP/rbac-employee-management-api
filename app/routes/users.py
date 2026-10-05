from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate
from app.security.auth import get_current_user
from app.services.user_service import (
    list_users,
    register_user,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/register",
    status_code=201,
)
def register(user: UserCreate):
    return register_user(user)


@router.get("/")
def get_users(current_user=Depends(get_current_user)):
    return {
        "current_user": {
            "id": str(current_user["_id"]),
            "name": current_user["name"],
            "role": current_user["role"],
        },
        "users": list_users(),
    }
