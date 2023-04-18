from datetime import date

from sqlalchemy.orm import Session

from . import models


def create(classroom_id: int, student_id: int, db: Session):
    today = date.today()
    new_attendance = models.Attendance(classroom_id=classroom_id, student_id=student_id, attended=True, date=today)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance


# quiero obtener todas las asistencias de un classroom_id y un rango de fechas
def get_list_by_classroom_id_and_date_range(classroom_id: int, start_date: str, end_date: str, db: Session):
    attendances = db.query(models.Attendance).filter(models.Attendance.classroom_id == classroom_id).filter(
        models.Attendance.date.between(start_date, end_date)).all()
    return attendances
