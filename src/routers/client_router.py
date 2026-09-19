from fastapi import APIRouter, Depends
from schemas.responses.client_response import ClientResponse
from src.entities.client import Client
from src.schemas.requests.client_request import ClientRequest
from src.dependencies.dependency_client_service import get_client_service


router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponse)
def create_client(request: ClientRequest, service = Depends(get_client_service)):
    
    client = Client(id=None, name=request.name, email=request.email, phone=request.phone)

    client_created = service.create_client(client)

    return {
        "message": "Cliente creado correctamente",
        "client": client_created
    }



@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, service = Depends(get_client_service)):
    client = service.get_by_id(client_id)
    return client