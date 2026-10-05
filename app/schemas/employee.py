from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )
    email: str
    department: str
    salary: float = Field(
        gt=0
    )


class EmployeeUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    department: str | None = None
    salary: float | None = Field(
        default=None,
        gt=0,
    )
