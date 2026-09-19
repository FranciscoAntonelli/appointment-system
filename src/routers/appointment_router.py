from fastapi import APIRouter, Depends
from src.schemas.requests.appointment_request import AppointmentRequest
from src.schemas.responses.appointment_response import AppointmentResponse
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

@router.post("/", response_model=AppointmentResponse) # esta funcion responde a peticiones HTTP POST
# fastapi toma automaticamente el json enviado por el cliente y lo convierte en un objeto AppointmentRequest
# depends le dice a fastapi antes de ejecutar, llama get_appointment_service y pasame el resultado de la variable service
def create_appointment(request: AppointmentRequest, service = Depends(get_appointment_service)):

    appointment = service.create_appointment(
        request.professional_id,
        request.client_id,
        request.datetime_slot
    )

    return {
        "message": "Turno creado correctamente",
        "appointment_id": appointment.id
    }
    

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    return service.get_by_id(appointment_id)



@router.patch("/{appointment_id}/confirm")
def confirm_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    return service.confirm_appointment(appointment_id)

@router.patch("/{appointment_id}/cancel")
def cancel_appointment(appointment_id: int, service = Depends(get_appointment_service)):
    return service.cancel_appointment(appointment_id)