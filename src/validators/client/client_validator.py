from src.exceptions.client_exception import ClientException
from src.validators.validator import Validator


class ClientValidator(Validator):

    def validate(self, client):
        self._validate_is_empty(client.name, "nombre")
        self._validate_is_empty(client.email, "email")
        self._validate_email(client.email)

    def _validate_is_empty(self, data, field_name):
        if not data:
             raise ClientException(f"El {field_name} está vacio")
        
    def _validate_email(self, email):
        count_at = 0
        at_position = 0

        for pos, char in enumerate(email):
            if char == "@":
                count_at += 1
                at_position = pos

        
        if count_at != 1:
            raise ClientException("Tiene que tener exactamente un @")

        if at_position == 0:
            raise ClientException("Tiene que haber texto antes del @")

        if at_position == len(email) - 1:
            raise ClientException("Tiene que haber un dominio despues del @")
        
        point_position = 0

        for pos in range(at_position + 1, len(email)):
            if email[pos] == ".":
                if pos + 1 < len(email) and email[pos + 1] == ".":
                    raise ClientException("No puede haber dos puntos seguidos en el dominio")
                
                point_position = pos
                break

        if point_position == 0:
            raise ClientException("El dominio tiene que tener un punto")

        if point_position == at_position + 1:
            raise ClientException("Tiene que haber texto entre el @ y el punto")

        if point_position == len(email) - 1:
            raise ClientException("Tiene que haber texto despues del punto")

        

    


