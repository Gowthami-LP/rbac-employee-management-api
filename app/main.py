from fastapi import FastAPI

from pymongo.errors import PyMongoError

from app.database.mongodb import check_database_connection
from app.routes.auth import router as auth_router
from app.routes.employees import router as employees_router
from app.routes.users import router as users_router

app = FastAPI(
    title="RBAC Employee Management API",
    description="Employee Management API with Role-Based Access Control",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(employees_router)


@app.get("/")
def root():
    return {
        "message": "RBAC Employee Management API is running"
    }


@app.get("/health")
def health_check():
    try:
        check_database_connection()
        return {
            "status": "healthy",
            "database": "connected",
        }
    except PyMongoError:
        return {
            "status": "unhealthy",
            "database": "disconnected",
        }
