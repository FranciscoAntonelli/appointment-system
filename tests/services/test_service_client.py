from unittest.mock import Mock

import pytest

from src.exceptions.not_found_exception import NotFoundException
from src.entities.client import Client
from src.services.client.service_client import ServiceClient


def test_get_by_id_returns_client():

    client = Client(
        id=1,
        name="Juan Perez",
        email="juan@gmail.com",
        phone="123456789"
    )

    mock_repo = Mock()
    mock_repo.get_by_id.return_value = client

    mock_validator = Mock()

    service = ServiceClient(mock_repo, mock_validator)

    result = service.get_by_id(1)

    assert result == client

def test_get_by_id_raises_exception_when_client_not_exists():

    mock_repo = Mock()
    mock_repo.get_by_id.return_value = None

    mock_validator = Mock()

    service = ServiceClient(mock_repo, mock_validator)

    with pytest.raises(NotFoundException, match="No existe el cliente"):
        service.get_by_id(999)