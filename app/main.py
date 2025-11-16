from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auth API",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/v1")