ROLE_PERMISSIONS = {
    "admin": {
        "user:create",
        "user:read",
        "user:update",
        "user:delete",
        "employee:create",
        "employee:read",
        "employee:update",
        "employee:delete",
        "report:read",
    },
    "manager": {
        "employee:create",
        "employee:read",
        "employee:update",
        "report:read",
    },
    "employee": {
        "employee:read",
    },
    "viewer": {
        "report:read",
    },
}
