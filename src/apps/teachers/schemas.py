from pydantic import BaseModel


class TeacherBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class TeacherCreate(TeacherBase):
    password: str


class Teacher(TeacherBase):
    id: int

    # classrooms: list[Classroom] = []

    class Config:
        orm_mode = True
