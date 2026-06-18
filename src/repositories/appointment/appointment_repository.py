from abc import ABC, abstractmethod


class AppointmentRepository(ABC):

    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def save(self, appointment):
        pass

    @abstractmethod
    def find_by_professional_and_datetime(self, professionla, datetime):
        pass

    @abstractmethod
    def get_by_id(self, appointment_id):
        pass