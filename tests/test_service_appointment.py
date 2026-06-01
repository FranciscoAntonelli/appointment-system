from unittest.mock import Mock

from entities.appointment import Appointment
from entities.professional import Professional
from services.appointment.service_appointment import ServiceAppointment
from datetime import datetime

from state.canceled_state import CanceledState
from state.pending_state import PendingState

def test_check_availability_returns_true_when_is_no_appointment():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "monday": ["09:00-12:00", "14:00-18:00"],
            "tuesday": ["09:00-13:00"],
            "wednesday": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    mock_professional_service.check_working_hours.return_value = True

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = None

    service_appointment = ServiceAppointment(mock_professional_service, mock_appointment_repo)

    assert service_appointment.check_availability(professional, datetime_slot)

def test_check_availability_returns_true_when_slot_is_canceled():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "monday": ["09:00-12:00", "14:00-18:00"],
            "tuesday": ["09:00-13:00"],
            "wednesday": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    mock_professional_service.check_working_hours.return_value = True

    appointment = Appointment(
        id=None,
        professional_id=1,
        duration=30,
        client_id=10,
        state=CanceledState()
    )

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = appointment

    service_appointment = ServiceAppointment(mock_professional_service, mock_appointment_repo)

    assert service_appointment.check_availability(professional, datetime_slot)

def test_check_availability_returns_false_when_slot_is_outside_working_hours():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "monday": ["09:00-12:00", "14:00-18:00"],
            "tuesday": ["09:00-13:00"],
            "wednesday": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    mock_professional_service.check_working_hours.return_value = False

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = None

    service_appointment = ServiceAppointment(mock_professional_service, mock_appointment_repo)

    assert not service_appointment.check_availability(professional, datetime_slot)



def test_check_availability_returns_false_when_slot_is_busy():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "monday": ["09:00-12:00", "14:00-18:00"],
            "tuesday": ["09:00-13:00"],
            "wednesday": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    mock_professional_service.check_working_hours.return_value = True

    appointment = Appointment(
        id=None,
        professional_id=1,
        duration=30,
        client_id=10,
        state=PendingState()
    )

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = appointment

    service_appointment = ServiceAppointment(mock_professional_service, mock_appointment_repo)

    assert not service_appointment.check_availability(professional, datetime_slot)


