import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    mongo_uri: str = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017",
    )

    mongo_database: str = os.getenv(
        "MONGO_DATABASE",
        "rbac_employee_db",
    )

    jwt_secret_key: str = os.getenv(
        "JWT_SECRET_KEY",
        "development-secret",
    )

    jwt_algorithm: str = os.getenv(
        "JWT_ALGORITHM",
        "HS256",
    )

    jwt_access_token_expire_minutes: int = int(
        os.getenv(
            "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
            "60",
        )
    )


settings = Settings()
