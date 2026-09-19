import pytest
from pydantic import ValidationError

from schemas.request.client_request import ClientRequest


def test_client_request_accepts_valid_data():
    client = ClientRequest(
        name="Juan Pérez",
        email="juan@gmail.com",
        phone="1123456789"
    )

    assert client.name == "Juan Pérez"
    assert client.email == "juan@gmail.com"
    assert client.phone == "1123456789"


def test_client_request_rejects_invalid_email():
    with pytest.raises(ValidationError):
        ClientRequest(
            name="Juan Pérez",
            email="juan-email",
            phone="1123456789"
        )


def test_client_request_rejects_empty_name():
    with pytest.raises(ValidationError):
        ClientRequest(
            name="",
            email="juan@gmail.com",
            phone="1123456789"
        )


def test_client_request_rejects_empty_phone():
    with pytest.raises(ValidationError):
        ClientRequest(
            name="Juan Pérez",
            email="juan@gmail.com",
            phone=""
        )


def test_client_request_rejects_missing_email():
    with pytest.raises(ValidationError):
        ClientRequest(
            name="Juan Pérez",
            phone="1123456789"
        )