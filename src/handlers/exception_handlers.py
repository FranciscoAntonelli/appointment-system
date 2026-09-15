from fastapi import Request
from fastapi.responses import JSONResponse

from src.exceptions.already_exists_exception import AlreadyExistsException
from src.exceptions.not_found_exception import NotFoundException
from src.exceptions.validation_exception import ValidationException
from src.exceptions.conflict_exception import ConflictException

# los handlers son funciones que se ejecutan cuando ocurre una excepcion, y devuelven una respuesta HTTP con el codigo de error correspondiente


def not_found_exception_handler(
    request: Request,   #request es el que recibe la peticion HTTP, no se usa pero es necesario para que fastapi lo reconozca como handler
    exc: NotFoundException
):
    return JSONResponse( #construye la respuesta HTTP en formato JSON.
        status_code=404,
        content={"detail": str(exc)}
    )


def validation_exception_handler(
    request: Request,
    exc: ValidationException
):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )


def conflict_exception_handler(
    request: Request,
    exc: ConflictException
):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)}
    )


def already_exists_exception_handler(
    request: Request,
    exc: AlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)}
    )