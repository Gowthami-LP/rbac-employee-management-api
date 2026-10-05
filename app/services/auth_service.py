from fastapi import HTTPException, status

from app.repositories.user_repository import find_user_by_email
from app.security.jwt import create_access_token
from app.security.password import verify_password


def login_user(email: str, password: str) -> dict[str, str]:
    user = find_user_by_email(email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    password_valid = verify_password(
        password,
        user["password"],
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(
        str(user["_id"]),
        user["role"],
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
