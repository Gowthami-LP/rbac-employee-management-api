from fastapi import HTTPException, status

from app.repositories.employee_repository import (
    create_employee,
    delete_employee,
    get_employee,
    get_employees,
    update_employee,
)
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee_service(data: EmployeeCreate) -> dict:
    employee = {
        "name": data.name,
        "email": data.email,
        "department": data.department,
        "salary": data.salary,
    }

    employee_id = create_employee(employee)

    return {
        "id": employee_id,
        **employee,
    }


def get_all_employees() -> list[dict]:
    employees = get_employees()

    return [
        {
            "id": str(employee["_id"]),
            "name": employee["name"],
            "email": employee["email"],
            "department": employee["department"],
            "salary": employee["salary"],
        }
        for employee in employees
    ]


def get_one_employee(employee_id: str) -> dict:
    employee = get_employee(employee_id)

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "department": employee["department"],
        "salary": employee["salary"],
    }


def update_employee_service(
    employee_id: str,
    data: EmployeeUpdate,
) -> dict:
    update_data = data.model_dump(
        exclude_none=True
    )

    result = update_employee(
        employee_id,
        update_data,
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return get_one_employee(employee_id)


def delete_employee_service(employee_id: str) -> dict[str, str]:
    result = delete_employee(employee_id)

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return {
        "message": "Employee deleted successfully"
    }
