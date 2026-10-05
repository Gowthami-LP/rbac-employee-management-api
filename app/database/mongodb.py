from pymongo import MongoClient

from app.config.settings import settings

client = MongoClient(settings.mongo_uri)

database = client[settings.mongo_database]

users_collection = database["users"]
roles_collection = database["roles"]
permissions_collection = database["permissions"]
employees_collection = database["employees"]


def check_database_connection() -> bool:
    client.admin.command("ping")
    return True
