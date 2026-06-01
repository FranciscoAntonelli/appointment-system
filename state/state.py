from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def blocks_schedule():
        pass