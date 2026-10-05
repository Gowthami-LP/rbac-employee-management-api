from fastapi import APIRouter, Depends

from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.security.rbac import require_permission
from app.services.employee_service import (
    create_employee_service,
    delete_employee_service,
    get_all_employees,
    get_one_employee,
    update_employee_service,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.post(
    "/",
    dependencies=[
        Depends(require_permission("employee:create"))
    ],
)
def create_employee(
    data: EmployeeCreate,
):
    return create_employee_service(data)


@router.get(
    "/",
    dependencies=[
        Depends(require_permission("employee:read"))
    ],
)
def get_employees():
    return get_all_employees()


@router.get(
    "/{employee_id}",
    dependencies=[
        Depends(require_permission("employee:read"))
    ],
)
def get_employee(
    employee_id: str,
):
    return get_one_employee(employee_id)


@router.put(
    "/{employee_id}",
    dependencies=[
        Depends(require_permission("employee:update"))
    ],
)
def update_employee(
    employee_id: str,
    data: EmployeeUpdate,
):
    return update_employee_service(
        employee_id,
        data,
    )


@router.delete(
    "/{employee_id}",
    dependencies=[
        Depends(require_permission("employee:delete"))
    ],
)
def delete_employee(
    employee_id: str,
):
    return delete_employee_service(employee_id)
