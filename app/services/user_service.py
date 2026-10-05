from fastapi import HTTPException, status

from app.repositories.user_repository import (
    create_user,
    find_user_by_email,
    get_all_users,
)
from app.schemas.user import UserCreate
from app.security.password import hash_password

VALID_ROLES = {
    "admin",
    "manager",
    "employee",
    "viewer",
}


def register_user(user_data: UserCreate) -> dict[str, str]:
    existing_user = find_user_by_email(
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    if user_data.role not in VALID_ROLES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid role",
        )

    hashed_password = hash_password(
        user_data.password
    )

    document = {
        "name": user_data.name,
        "email": user_data.email,
        "password": hashed_password,
        "role": user_data.role,
    }

    user_id = create_user(document)

    return {
        "id": str(user_id),
        "name": document["name"],
        "email": document["email"],
        "role": document["role"],
    }


def list_users() -> list[dict[str, str]]:
    users = get_all_users()

    result = []

    for user in users:
        result.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
        })

    return result
