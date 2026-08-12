from fastapi import APIRouter, Depends, HTTPException
from src.schemas.client_request import ClientRequest
from src.dependencies.dependency_client_service import get_client_service


router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/")
def create_client(request: ClientRequest, service = Depends(get_client_service)):
    
    try:

        client = service.c

    except: