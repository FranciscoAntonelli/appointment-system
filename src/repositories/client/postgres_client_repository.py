from src.exceptions.already_exists_exception import AlreadyExistsException
from src.repositories.client.client_repository import ClientRepository
from src.entities.client import Client
from psycopg2.errors import UniqueViolation

class PostgresClientRepository(ClientRepository):

    def __init__(self, connection):
        super().__init__(connection)

    def get_by_id(self, client_id):
        
        cursor = None

        try:

            cursor = self._connection.cursor()

            cursor.execute(
                """
                SELECT *
                FROM clients
                where id = %s
                """,
                (client_id,)
            )

            row = cursor.fetchone()

            if not row:
                return None
            
            return Client(id=row[0], name=row[1], email=row[2], phone=row[3])

        finally:
            if cursor:
                cursor.close()


    def save(self, client):
        cursor = None

        try:

            cursor = self._connection.cursor()

            cursor.execute(
                """
                INSERT INTO clients (name, email, phone)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (client.name, client.email, client.phone)
            )

            client_id = cursor.fetchone()[0]

            self._connection.commit()

            return client_id

        except UniqueViolation:
            self._connection.rollback()
            raise AlreadyExistsException("El email ya está registrado")

        except Exception:
            self._connection.rollback()
            raise

        finally:
            if cursor:
                cursor.close()