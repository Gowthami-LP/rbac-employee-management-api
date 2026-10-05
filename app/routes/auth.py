from fastapi import APIRouter

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(request: LoginRequest) -> dict[str, str]:
    return login_user(
        request.email,
        request.password,
    )
