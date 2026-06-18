from fastapi import APIRouter, Depends, HTTPException

from src.exceptions.professional_exception import ProfessionalException
from src.exceptions.available_exception import AvailableException
from src.exceptions.client_exception import ClientException
from src.schemas.appointment_request import AppointmentRequest
from src.dependencies.dependency_appointment_service import get_appointment_service

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# en fastapi se ponen los tipos

@router.post("/")
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
        raise HTTPException(status_code=404, detail=str(e))
    
    except AvailableException as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/{appointment_id}")
def get_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    
    try:
        appointment = service.get_by_id(appointment_id)

        return appointment

    except AvailableException as e:
        raise HTTPException(status_code=404, detail=str(e))