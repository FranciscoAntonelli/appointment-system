from fastapi import FastAPI
from src.routers.appointment_router import router as appointment_router
from src.routers.professional_router import router as professional_router
from src.routers.client_router import router as client_router

from src.exceptions.not_found_exception import NotFoundException
from src.exceptions.validation_exception import ValidationException
from src.exceptions.conflict_exception import ConflictException
from src.exceptions.already_exists_exception import AlreadyExistsException

from src.handlers.exception_handlers import (
    not_found_exception_handler,
    validation_exception_handler,
    conflict_exception_handler,
    already_exists_exception_handler
)

# uvicorn src.main:app --reload

app = FastAPI() #crea una app web

app.add_exception_handler(NotFoundException, not_found_exception_handler) # le dice a fastapi que cuando ocurra una excepcion NotFoundException, llame a la funcion not_found_exception_handler
app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(ConflictException, conflict_exception_handler)
app.add_exception_handler(AlreadyExistsException, already_exists_exception_handler)

app.include_router(appointment_router) #le registra al objeto app todas las rutas definidas en appointment_router
app.include_router(professional_router)
app.include_router(client_router)