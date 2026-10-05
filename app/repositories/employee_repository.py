from bson import ObjectId
from bson.errors import InvalidId

from app.database.mongodb import employees_collection


def _employee_id_query(employee_id: str) -> dict:
    try:
        object_id = ObjectId(employee_id)
    except InvalidId:
        return {"_id": employee_id}

    return {
        "_id": {
            "$in": [employee_id, object_id]
        }
    }


def create_employee(employee: dict) -> str:
    result = employees_collection.insert_one(employee)

    return str(result.inserted_id)


def get_employees() -> list:
    return list(
        employees_collection.find({})
    )


def get_employee(employee_id: str):
    return employees_collection.find_one(
        _employee_id_query(employee_id)
    )


def update_employee(
    employee_id: str,
    update_data: dict,
):
    return employees_collection.update_one(
        _employee_id_query(employee_id),
        {"$set": update_data},
    )


def delete_employee(employee_id: str):
    return employees_collection.delete_one(
        _employee_id_query(employee_id)
    )
