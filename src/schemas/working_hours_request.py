from pydantic import BaseModel, Field
from datetime import time

class WorkingHoursRequest(BaseModel):
    day_of_week: str = Field(min_length=1, max_length=20)
    start_time: time
    end_time: time