from fastapi import APIRouter, Depends
from schemas.responses.professional_response import ProfessionalResponse
from src.entities.professional import Professional
from src.schemas.requests.professional_request import ProfessionalRequest
from src.dependencies.dependency_professional_service import get_professional_service


router = APIRouter(prefix="/professionals", tags=["Professionals"])

@router.post("/", response_model=ProfessionalResponse)
def create_professional(request: ProfessionalRequest, service = Depends(get_professional_service)):


    professional = Professional(id=None, name=request.name, specialty=request.specialty, 
                                working_hours=request.working_hours, 
                                default_duration_minutes=request.default_duration_minutes)
        
    professional_created = service.create_professional(professional)

    return {
         "message": "Professional creado correctamente",
        "professional_id": professional_created.id
    }
    

@router.get("/{professional_id}", response_model=ProfessionalResponse)
def get_professional(professional_id: int, service = Depends(get_professional_service)):
    professional = service.get_by_id(professional_id)
    return professional