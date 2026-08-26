from datetime import datetime

from src.exceptions.validation_exception import ValidationException
from src.exceptions.not_found_exception import NotFoundException
from src.services.professional.i_service_professinal import IServiceProfessional


class ServiceProfessional(IServiceProfessional):
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator


    def create_professional(self, professional):

        self._validator.validate(professional)

        professional_id = self._repo.save(professional)

        professional.set_id(professional_id)

        return professional
    
    def get_by_id(self, professional_id):
        if professional_id is None:
            raise ValidationException("No hay ningun profesional seleccionado")

        professional = self._repo.get_by_id(professional_id)
        if not professional:
            raise NotFoundException("No existe ese profesional")

        return professional
        


        