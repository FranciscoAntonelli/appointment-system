from datetime import time
import pytest

from src.entities.working_hours import WorkingHours
from src.exceptions.validation_exception import ValidationException
from src.validators.professional.working_hours_validator import WorkingHoursValidator


def test_validate_works_well():

    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(14, 0), time(18, 0)),
        WorkingHours("Martes", time(9, 0), time(13, 0)),
    ]

    validator = WorkingHoursValidator()

    validator.validate(working_hours)


def test_validate_returns_error_when_working_hours_is_empty():

    validator = WorkingHoursValidator()

    with pytest.raises(ValidationException):
        validator.validate([])


def test_validate_returns_error_when_day_is_invalid():

    working_hours = [
        WorkingHours("Luness", time(9, 0), time(12, 0))
    ]

    validator = WorkingHoursValidator()

    with pytest.raises(ValidationException):
        validator.validate(working_hours)


def test_validate_returns_error_when_start_time_is_greater_than_end_time():

    working_hours = [
        WorkingHours("Lunes", time(13, 0), time(12, 0))
    ]

    validator = WorkingHoursValidator()

    with pytest.raises(ValidationException):
        validator.validate(working_hours)


def test_validate_returns_error_when_schedules_overlap():

    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(11, 0), time(18, 0))
    ]

    validator = WorkingHoursValidator()

    with pytest.raises(ValidationException):
        validator.validate(working_hours)


def test_validate_accepts_non_overlapping_schedules():

    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(12, 0), time(18, 0))
    ]

    validator = WorkingHoursValidator()

    validator.validate(working_hours)


