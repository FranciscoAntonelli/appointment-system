from pydantic import BaseModel
from datetime import time

class WorkingHoursRequest(BaseModel):
    day_of_week: str
    start_time: time
    end_time: time