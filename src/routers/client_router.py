from fastapi import APIRouter, Depends, HTTPException
from src.exceptions.not_found_exception import NotFoundException
from src.entities.client import Client
from src.exceptions.validation_exception import ValidationException
from src.exceptions.already_exists_exception import AlreadyExistsException
from src.schemas.client_request import ClientRequest
from src.dependencies.dependency_client_service import get_client_service


router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/")
def create_client(request: ClientRequest, service = Depends(get_client_service)):
    
    try:

        client = Client(id=None, name=request.name, email=request.email, phone=request.phone)

        client_created = service.create_client(client)

        return {
            "message": "Cliente creado correctamente",
            "client": client_created
        }

    except(ValidationException) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except(AlreadyExistsException) as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/{client_id}")
def get_client(client_id: int, service = Depends(get_client_service)):
    
    try:
        client = service.get_by_id(client_id)
        return client
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))