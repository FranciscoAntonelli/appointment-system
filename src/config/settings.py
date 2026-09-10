import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    def __init__(self):
        self._db_host = os.getenv("DB_HOST")
        self._db_name = os.getenv("DB_NAME")
        self._db_user = os.getenv("DB_USER")
        self._db_password = os.getenv("DB_PASSWORD")

settings = Settings()