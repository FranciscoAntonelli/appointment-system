from pydantic import BaseModel # sirve para validar datos automaticamente, convertir json a objetos python
from datetime import datetime

#schema de entrada que fastapi usa para validar los datos que le llegan de la peticion

class AppointmentRequest(BaseModel): #esta clase representa datos que vienen de una peticion
    professional_id: int
    client_id: int
    datetime_slot: datetime