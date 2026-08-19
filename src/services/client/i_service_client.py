from abc import ABC, abstractmethod


class IServiceClient(ABC):
    def __init__(self, client_repo):
        self._client_repo = client_repo

    @abstractmethod
    def get_by_id(self, client_id):
        pass

    @abstractmethod
    def create_client(self, client):
        pass