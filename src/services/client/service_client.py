from src.exceptions.not_found_exception import NotFoundException
from src.services.client.i_service_client import IServiceClient


class ServiceClient(IServiceClient):
    def __init__(self, client_repo, validator):
        self._client_repo = client_repo
        self._validator = validator

    def get_by_id(self, client_id):
        
        client = self._client_repo.get_by_id(client_id)

        if not client:
            raise NotFoundException("No existe el cliente")
        
        return client
    

    def create_client(self, client):

        self._validator.validate(client)

        client_id = self._client_repo.save(client)

        client.set_id(client_id)

        return client