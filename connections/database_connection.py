from abc import ABC, abstractmethod


class DatabaseConnection(ABC):

    def __init__(self, host, database, user, password):
        self._host = host
        self._database = database
        self._user = user
        self._password = password

    @abstractmethod
    def connect(self):
        pass