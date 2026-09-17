from abc import ABC, abstractmethod


class AppointmentRepository(ABC):

    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def save(self, appointment):
        pass

    @abstractmethod
    def find_conflicting_appointment(self, professional_id, start_datetime, end_datetime):
        pass

    @abstractmethod
    def get_by_id(self, appointment_id):
        pass