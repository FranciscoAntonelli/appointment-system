from src.repositories.client.client_repository import ClientRepository
from src.entities.client import Client


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