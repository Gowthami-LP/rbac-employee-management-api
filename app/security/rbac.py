from fastapi import Depends, HTTPException, status

from app.models.role import ROLE_PERMISSIONS
from app.security.auth import get_current_user


def require_permission(permission: str):
    def permission_checker(
        current_user=Depends(get_current_user),
    ):
        role = current_user["role"]

        role_permissions = ROLE_PERMISSIONS.get(
            role,
            set(),
        )

        if permission not in role_permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"Role '{role}' does not have "
                    f"permission '{permission}'"
                ),
            )

        return current_user

    return permission_checker
