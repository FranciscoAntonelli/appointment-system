from connections.postgres_connection import PostgresConnection
from src.config.settings import settings

def get_connection():

    connection = PostgresConnection(
        host=settings._db_host,
        database=settings._db_name,
        user=settings._db_user,
        password=settings._db_password
    ).connect()

    try:
        yield connection # yield es como un return pero permite que la funcion no se cierra la conexion a la base de datos y se puede seguir usando
    finally:
        connection.close()