from fastapi import FastAPI
from src.routers.appointment_router import router as appointment_router

app = FastAPI()

app.include_router(appointment_router)

# uvicorn src.main:app --reload