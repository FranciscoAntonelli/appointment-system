from connections.postgres_connection import PostgresConnection
from src.config.settings import settings

def get_connection():

    connection = PostgresConnection(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    ).connect()

    return connection