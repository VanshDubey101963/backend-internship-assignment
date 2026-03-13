from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth_routes, task_routes

app = FastAPI(title="Backend Assignment API")

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(task_routes.router)