from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

from src.schemas.requests.working_hours_request import WorkingHoursRequest

class ProfessionalRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    specialty: str = Field(min_length=1, max_length=100)
    default_duration_minutes: int = Field(gt=0)
    working_hours: List[WorkingHoursRequest] = Field(min_length=1) 