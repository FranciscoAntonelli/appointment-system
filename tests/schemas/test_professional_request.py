import pytest
from datetime import time
from pydantic import ValidationError

from schemas.request.professional_request import ProfessionalRequest
from schemas.request.working_hours_request import WorkingHoursRequest


def test_professional_request_accepts_valid_data():
    professional = ProfessionalRequest(
        name="Dr. Juan Pérez",
        specialty="Dermatología",
        default_duration_minutes=30,
        working_hours=[
            WorkingHoursRequest(
                day_of_week="Lunes",
                start_time=time(9, 0),
                end_time=time(18, 0)
            )
        ]
    )

    assert professional.name == "Dr. Juan Pérez"
    assert professional.specialty == "Dermatología"
    assert professional.default_duration_minutes == 30
    assert len(professional.working_hours) == 1


def test_professional_request_rejects_empty_name():
    with pytest.raises(ValidationError):
        ProfessionalRequest(
            name="",
            specialty="Dermatología",
            default_duration_minutes=30,
            working_hours=[
                WorkingHoursRequest(
                    day_of_week="Lunes",
                    start_time=time(9, 0),
                    end_time=time(18, 0)
                )
            ]
        )


def test_professional_request_rejects_empty_specialty():
    with pytest.raises(ValidationError):
        ProfessionalRequest(
            name="Dr. Juan Pérez",
            specialty="",
            default_duration_minutes=30,
            working_hours=[
                WorkingHoursRequest(
                    day_of_week="Lunes",
                    start_time=time(9, 0),
                    end_time=time(18, 0)
                )
            ]
        )


def test_professional_request_rejects_zero_duration():
    with pytest.raises(ValidationError):
        ProfessionalRequest(
            name="Dr. Juan Pérez",
            specialty="Dermatología",
            default_duration_minutes=0,
            working_hours=[
                WorkingHoursRequest(
                    day_of_week="Lunes",
                    start_time=time(9, 0),
                    end_time=time(18, 0)
                )
            ]
        )


def test_professional_request_rejects_empty_working_hours():
    with pytest.raises(ValidationError):
        ProfessionalRequest(
            name="Dr. Juan Pérez",
            specialty="Dermatología",
            default_duration_minutes=30,
            working_hours=[]
        )