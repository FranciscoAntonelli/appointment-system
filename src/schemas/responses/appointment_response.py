from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.enums.appointment_state import AppointmentState


class AppointmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    duration: int
    professional_id: int
    datetime_slot: datetime
    client_id: int
    state: AppointmentState