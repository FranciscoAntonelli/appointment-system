from datetime import time
import pytest

from src.entities.professional import Professional
from src.entities.working_hours import WorkingHours
from src.exceptions.validation_exception import ValidationException
from src.validators.professional.professional_validator import ProfessionalValidator
from src.validators.professional.working_hours_validator import WorkingHoursValidator


# --- tests de errores ---

def test_create_professional_returns_error_when_name_is_empty():
    professional = Professional(
        id=1,
        name="",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miércoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    with pytest.raises(ValidationException):
        validator.validate(professional)
    

def test_create_professional_returns_error_when_working_hours_is_empty():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[],
        default_duration_minutes=30
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    with pytest.raises(ValidationException):
        validator.validate(professional)


def test_create_professional_returns_error_when_duration_is_not_number():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miércoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes="asd"
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    with pytest.raises(ValidationException):
        validator.validate(professional)

def test_create_professional_returns_error_when_duration_is_negative_or_zero():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miércoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=0
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    with pytest.raises(ValidationException):
        validator.validate(professional)

def test_create_professional_returns_error_when_duration_exceed_the_limit():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miércoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=481
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    with pytest.raises(ValidationException):
        validator.validate(professional)



def test_validate_works_well():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0))
        ],
        default_duration_minutes=30
    )

    working_hours_validator = WorkingHoursValidator()

    validator = ProfessionalValidator(
        working_hours_validator
    )

    validator.validate(professional)