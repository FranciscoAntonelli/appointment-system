from pydantic import BaseModel, Field # sirve para validar datos automaticamente, convertir json a objetos python
from datetime import datetime

#schema de entrada que fastapi usa para validar los datos que le llegan de la peticion

class AppointmentRequest(BaseModel): #esta clase representa datos que vienen de una peticion
    professional_id: int = Field(gt=0) # le indico que el id del profesional debe ser mayor a 0
    client_id: int = Field(gt=0)
    datetime_slot: datetime