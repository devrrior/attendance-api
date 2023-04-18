from pydantic import BaseModel

from src.apps.attendances.schemas import Attendance


class StudentBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class StudentCreate(StudentBase):
    classroom_id: int


class StudentReadNested(StudentBase):
    pass

    class Config:
        orm_mode = True


class Student(StudentBase):
    id: int
    classroom_id: int
    attendances: list[Attendance] = []

    class Config:
        orm_mode = True
