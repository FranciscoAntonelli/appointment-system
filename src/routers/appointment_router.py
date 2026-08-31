from fastapi import APIRouter, Depends, HTTPException

from src.exceptions.validation_exception import ValidationException
from src.exceptions.professional_exception import ProfessionalException
from src.exceptions.available_exception import AvailableException
from src.exceptions.client_exception import ClientException
from src.schemas.appointment_request import AppointmentRequest
from src.dependencies.dependency_appointment_service import get_appointment_service

"""
    200 → OK
    201 → Creado
    400 → Solicitud incorrecta
    404 → No encontrado
    409 → Conflicto
    500 → Error interno
    """

router = APIRouter(prefix="/appointments", tags=["Appointments"]) #crea router FastApi

# en fastapi se ponen los tipos

@router.post("/") # esta funcion responde a peticiones HTTP POST
# fastapi toma automaticamente el json enviado por el cliente y lo convierte en un objeto AppointmentRequest
# depends le dice a fastapi antes de ejecutar, llama get_appointment_service y pasame el resultado de la variable service
def create_appointment(request: AppointmentRequest, service = Depends(get_appointment_service)):

    try:

        appointment = service.create_appointment(
            request.professional_id,
            request.client_id,
            request.datetime_slot
        )

        return {
            "message": "Turno creado correctamente",
            "appointment_id": appointment.id
        }

    except (ProfessionalException, ClientException) as e:
        raise HTTPException(status_code=404, detail=str(e)) # detiene la ejecucion y devuelve una respuesta HTTP de error
    
    except AvailableException as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/{appointment_id}")
def get_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    
    try:
        appointment = service.get_by_id(appointment_id)

        return appointment

    except AvailableException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{appointment_id}/confirm")
def confirm_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    try:
        return service.confirm_appointment(appointment_id)
    except AvailableException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationException as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{appointment_id}/cancel")
def cancel_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    try:
        return service.cancel_appointment(appointment_id)
    except AvailableException as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationException as e:
            raise HTTPException(status_code=400, detail=str(e))