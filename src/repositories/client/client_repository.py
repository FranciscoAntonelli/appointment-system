from abc import ABC, abstractmethod


class ClientRepository(ABC):

    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def get_by_id(self, client_id):
        pass

    @abstractmethod
    def save(self, client):
        pass