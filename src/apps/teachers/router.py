from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database.session import get_db

from . import service
from .schemas import TeacherCreate, Teacher

router = APIRouter(
    prefix="/teachers",
    tags=["teachers"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=Teacher)
def create(request: TeacherCreate, db: Session = Depends(get_db)):
    teacher_exists = service.get_by_email(request.email, db)

    if teacher_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_teacher = service.create(request, db)
    return new_teacher


@router.get("/{email}", response_model=Teacher)
def get_by_email(email: str, db: Session = Depends(get_db)):
    teacher = service.get_by_email(email, db)

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return teacher
