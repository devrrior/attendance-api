from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.apps.auth.dependecies import get_current_user
from src.apps.teachers.schemas import Teacher
from src.database.session import get_db
from src.utils.email_service import EmailService
from src.utils.qr_generator import QRGenerator
from . import service as student_service
from src.apps.classrooms import service as classroom_service
from .schemas import StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create(request: StudentCreate, current_user: Teacher = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    student_exists = student_service.get_by_email(request.email, db)

    if student_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    print(request.classroom_id)
    classroom = classroom_service.get_by_id(request.classroom_id, db)

    if classroom is None:
        raise HTTPException(status_code=400, detail="Classroom not found")

    if classroom.teacher_id != current_user.id:
        raise HTTPException(status_code=400, detail="You are not the teacher of this classroom")

    student = student_service.create(request, db)

    url = f"http://localhost:8000/attendance/student/{student.id}"

    qr_file = QRGenerator.generate_qr_code(url)
    EmailService.send_email_with_qr_code(qr_file, student.email)

    return student
