from src.exceptions.client_exception import ClientException
from src.services.client.i_service_client import IServiceClient


class ServiceClient(IServiceClient):
    def __init__(self, client_repo):
        super().__init__(client_repo)

    def get_by_id(self, client_id):
        
        client = self._client_repo.get_by_id(client_id)

        if not client:
            raise ClientException("No existe el cliente")
        
        return client
    

    def create_client(self, client):

        self._