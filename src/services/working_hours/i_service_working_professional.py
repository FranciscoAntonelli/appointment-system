from abc import ABC, abstractmethod


class IServiceWorkingHours(ABC):

    @abstractmethod
    def is_within_schedule(self, working_hours, datetime_slot):
        pass