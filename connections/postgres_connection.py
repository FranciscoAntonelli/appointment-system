import psycopg2

from connections.database_connection import DatabaseConnection

class PostgresConnection(DatabaseConnection):

    def __init__(self, host, database, user, password):
        super().__init__(host, database, user, password)

    def connect(self):
        return psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._user,
            password=self._password
        )