from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import users_collection


def find_user_by_email(email: str):
    return users_collection.find_one({
        "email": email
    })


def find_user_by_id(user_id: str):
    try:
        object_id = ObjectId(user_id)
    except InvalidId:
        object_id = None

    if object_id is None:
        query = {"_id": user_id}
    else:
        query = {
            "_id": {
                "$in": [user_id, object_id]
            }
        }

    return users_collection.find_one(query)


def create_user(user_data: dict):
    result = users_collection.insert_one(user_data)

    return result.inserted_id


def get_all_users():
    return list(
        users_collection.find(
            {},
            {
                "password": 0
            },
        )
    )
