from abc import ABC, abstractmethod

class IServiceProfessional(ABC):
    def __init__(self, repo):
        self._repo = repo

    @abstractmethod
    def create_professional(self, professional):
        pass

    @abstractmethod
    def get_by_id(self, professional_id):
        pass

    @abstractmethod
    def check_working_hours(self, professional, datetime_slot):
        pass