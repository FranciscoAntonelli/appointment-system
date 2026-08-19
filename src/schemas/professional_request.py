from typing import List

from pydantic import BaseModel
from datetime import datetime

from src.schemas.working_hours_request import WorkingHoursRequest

class ProfessionalRequest(BaseModel):
    name: str
    specialty: str
    default_duration_minutes: int
    working_hours: List[WorkingHoursRequest]