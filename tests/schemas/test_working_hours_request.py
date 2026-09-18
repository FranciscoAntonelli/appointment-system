import pytest
from datetime import time
from pydantic import ValidationError

from src.schemas.working_hours_request import WorkingHoursRequest


def test_working_hours_request_accepts_valid_data():
    working_hours = WorkingHoursRequest(
        day_of_week="Lunes",
        start_time=time(9, 0),
        end_time=time(18, 0)
    )

    assert working_hours.day_of_week == "Lunes"
    assert working_hours.start_time == time(9, 0)
    assert working_hours.end_time == time(18, 0)


def test_working_hours_request_rejects_empty_day():
    with pytest.raises(ValidationError):
        WorkingHoursRequest(
            day_of_week="",
            start_time=time(9, 0),
            end_time=time(18, 0)
        )


def test_working_hours_request_rejects_invalid_start_time():
    with pytest.raises(ValidationError):
        WorkingHoursRequest(
            day_of_week="Lunes",
            start_time="hora-invalida",
            end_time=time(18, 0)
        )


def test_working_hours_request_rejects_invalid_end_time():
    with pytest.raises(ValidationError):
        WorkingHoursRequest(
            day_of_week="Lunes",
            start_time=time(9, 0),
            end_time="hora-invalida"
        )