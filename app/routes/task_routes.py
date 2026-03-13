from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.task_schema import TaskCreate
from app.models.task_model import Task
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_task(task: TaskCreate,
                user=Depends(get_current_user),
                db: Session = Depends(get_db)):

    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=user["id"]
    )

    db.add(new_task)
    db.commit()

    return {"message": "Task created"}


@router.get("/")
def get_tasks(user=Depends(get_current_user),
              db: Session = Depends(get_db)):

    return db.query(Task).filter(Task.owner_id == user["id"]).all()