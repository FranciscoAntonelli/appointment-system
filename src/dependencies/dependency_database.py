from connections.postgres_connection import PostgresConnection
from src.config.settings import settings

def get_connection():

    connection = PostgresConnection(
        host=settings._db_host,
        database=settings._db_name,
        user=settings._db_user,
        password=settings._db_password
    ).connect()

    return connection