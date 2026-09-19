import pytest
from datetime import datetime
from pydantic import ValidationError

from schemas.request.appointment_request import AppointmentRequest


def test_appointment_request_accepts_valid_data():
    appointment = AppointmentRequest(
        professional_id=1,
        client_id=10,
        datetime_slot=datetime(2026, 5, 18, 10, 0)
    )

    assert appointment.professional_id == 1
    assert appointment.client_id == 10
    assert appointment.datetime_slot == datetime(2026, 5, 18, 10, 0)


def test_appointment_request_rejects_invalid_professional_id():
    with pytest.raises(ValidationError):
        AppointmentRequest(
            professional_id=0,
            client_id=10,
            datetime_slot=datetime(2026, 5, 18, 10, 0)
        )


def test_appointment_request_rejects_negative_client_id():
    with pytest.raises(ValidationError):
        AppointmentRequest(
            professional_id=1,
            client_id=-1,
            datetime_slot=datetime(2026, 5, 18, 10, 0)
        )


def test_appointment_request_rejects_missing_datetime():
    with pytest.raises(ValidationError):
        AppointmentRequest(
            professional_id=1,
            client_id=10
        )