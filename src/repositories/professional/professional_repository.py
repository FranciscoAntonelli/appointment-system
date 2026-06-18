from abc import ABC, abstractmethod


class ProfessionalRepository(ABC):
    
   def __init__(self, connection):
      self._connection = connection

   @abstractmethod
   def save(self, professional):
      pass
    

   @abstractmethod
   def get_by_id(self, professional_id):
      pass