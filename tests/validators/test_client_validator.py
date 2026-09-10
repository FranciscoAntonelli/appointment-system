from datetime import time
import pytest

from src.exceptions.validation_exception import ValidationException
from src.entities.client import Client
from src.validators.client.client_validator import ClientValidator


def test_valid_email_successfully():
    client = Client(
        id=1,
        name="Juan Perez",
        email="juan.perez@gmail.com",
        phone="1123456789"
    )

    client_validator = ClientValidator()

    client_validator.validate(client)


def test_valid_email_returns_error_when_name_is_empty():
    client = Client(
            id=1,
            name="",
            email="juan.perez@gmail.com",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_empty():
    client = Client(
            id=1,
            name="Juan",
            email="",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_two_at():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez@@gmail.com",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_no_text_before_at():
    client = Client(
            id=1,
            name="Juan",
            email="@gmail.com",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)

def test_valid_email_returns_error_when_email_is_invalid_for_no_text_after_at():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez@",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_consecutive_points():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez.@gmail..com",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_there_is_no_point():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez@gmail",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_no_text_between_at_and_point():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez@.com",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)


def test_valid_email_returns_error_when_email_is_invalid_for_no_text_after_point():
    client = Client(
            id=1,
            name="Juan",
            email="juan.perez@gmail.",
            phone="1123456789"
        )
    
    client_validator = ClientValidator()
    
    with pytest.raises(ValidationException):
        client_validator.validate(client)

