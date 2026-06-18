from abc import ABC, abstractmethod


class INotificationService(ABC):

    @abstractmethod
    def send_confirmation(self, appointment, professional):
        pass