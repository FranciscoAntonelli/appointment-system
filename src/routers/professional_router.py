from fastapi import APIRouter, Depends, HTTPException
from src.entities.professional import Professional
from src.exceptions.not_found_exception import NotFoundException
from src.exceptions.validation_exception import ValidationException
from src.exceptions.already_exists_exception import AlreadyExistsException
from src.schemas.professional_request import ProfessionalRequest
from src.dependencies.dependency_professional_service import get_professional_service


router = APIRouter(prefix="/professionals", tags=["Professionals"])

@router.post("/")
def create_professional(request: ProfessionalRequest, service = Depends(get_professional_service)):

    try:
        professional = Professional(id=None, name=request.name, specialty=request.specialty, 
                                    working_hours=request.working_hours, 
                                    default_duration_minutes=request.default_duration_minutes)
        
        professional_created = service.create_professional(professional)

        return {
            "message": "Professional creado correctamente",
            "professional_id": professional_created.id
        }

    except(ValidationException) as e:
            raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/{professional_id}")
def get_professional(professional_id: int, service = Depends(get_professional_service)):

    try:
        professional = service.get_by_id(professional_id)
        return professional
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))