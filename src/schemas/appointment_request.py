from pydantic import BaseModel
from datetime import datetime

class AppointmentRequest(BaseModel):
    professional_id: int
    client_id: int
    datetime_slot: datetime