from fastapi import FastAPI
from src.routers.appointment_router import router as appointment_router
from src.routers.professional_router import router as professional_router

# uvicorn src.main:app --reload

app = FastAPI() #crea una app web

app.include_router(appointment_router) #le registra al objeto app todas las rutas definidas en appointment_router
app.include_router(professional_router)