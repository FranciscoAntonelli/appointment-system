
from src.exceptions.validation_exception import ValidationException
from src.validators.validator import Validator


class ClientValidator(Validator):

    def validate(self, client):
        self._validate_is_empty(client.name, "nombre")
        self._validate_is_empty(client.email, "email")

    def _validate_is_empty(self, data, field_name):
        if not data:
             raise ValidationException(f"El {field_name} está vacio")