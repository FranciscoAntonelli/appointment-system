from abc import ABC, abstractmethod

class IServiceAppointment(ABC):

    @abstractmethod
    def check_availability(self, professional, datetime_slot):
        pass

    @abstractmethod
    def create_appointment(self, professional, client_id, datetime_slot):
        pass

    abstractmethod
    def get_by_id(self, appointment_id):
        pass