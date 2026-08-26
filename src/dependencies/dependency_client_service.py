from src.dependencies.dependency_database import get_connection
from src.repositories.client.postgres_client_repository import PostgresClientRepository
from src.services.client.service_client import ServiceClient
from src.validators.client.client_validator import ClientValidator


def get_client_service():

    connection = get_connection()

    repo = PostgresClientRepository(connection)
    validator = ClientValidator()

    return ServiceClient(repo, validator)