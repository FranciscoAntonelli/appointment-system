from src.exceptions.validation_exception import ValidationException
from src.validators.validator import Validator

class ProfessionalValidator(Validator):

    def __init__(self, working_hours_validator):
        self._working_hours_validator = working_hours_validator

    def validate(self, professional):
        self._validate_name(professional.name)
        self._validate_duration(professional.duration)
        self._working_hours_validator.validate(professional.working_hours)

    def _validate_name(self, name):
        if not name:
            raise ValidationException("No hay nombre")

    def _validate_duration(self, duration):

        if duration <= 0:
            raise ValidationException("La duración debe ser mayor a 0")
            
        if duration > 480:
            raise ValidationException("La duración no puede superar los 480 minutos (8 horas)")
