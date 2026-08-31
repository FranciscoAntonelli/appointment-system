from unittest.mock import Mock

import pytest

from src.exceptions.validation_exception import ValidationException
from src.exceptions.available_exception import AvailableException
from src.entities.working_hours import WorkingHours
from src.entities.appointment import Appointment
from src.entities.professional import Professional
from src.services.appointment.service_appointment import ServiceAppointment
from src.enums.appointment_state import AppointmentState
from datetime import datetime, time

# --- tests sin errores ---

def test_check_availability_returns_true_when_is_no_appointment():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional

    mock_notification_service = Mock()

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = None

    mock_working_hours_service = Mock()
    mock_working_hours_service.is_within_schedule.return_value = True

    mock_client_service = Mock()

    service_appointment = ServiceAppointment(mock_professional_service, mock_working_hours_service,
                                             mock_notification_service, mock_client_service, mock_appointment_repo)

    assert service_appointment.check_availability(professional, datetime_slot)

def test_check_availability_returns_true_when_slot_is_canceled():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    
    mock_working_hours_service = Mock()
    mock_working_hours_service.is_within_schedule.return_value = True

    mock_notification_service = Mock()

    mock_working_hours_service = Mock()
    mock_working_hours_service.is_within_schedule.return_value = True

    appointment = Appointment(
        id=None,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.CANCELED
    )

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = appointment

    mock_client_service = Mock()

    service_appointment = ServiceAppointment(mock_professional_service, mock_working_hours_service, mock_notification_service , mock_client_service, mock_appointment_repo)

    assert service_appointment.check_availability(professional, datetime_slot)


# --- tests de errores ---

def test_check_availability_returns_false_when_slot_is_outside_working_hours():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional

    mock_notification_service = Mock()

    mock_working_hours_service = Mock()
    mock_working_hours_service.is_within_schedule.return_value = False

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = None

    mock_client_service = Mock()

    service_appointment = ServiceAppointment(mock_professional_service, mock_working_hours_service,
                                              mock_notification_service, mock_client_service,  mock_appointment_repo)

    assert not service_appointment.check_availability(professional, datetime_slot)



def test_check_availability_returns_false_when_slot_is_busy():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_professional_service = Mock()
    mock_professional_service.get_by_id.return_value = professional
    
    mock_working_hours_service = Mock()
    mock_working_hours_service.is_within_schedule.return_value = True

    mock_notification_service = Mock()

    appointment = Appointment(
        id=None,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.PENDING
    )

    mock_appointment_repo = Mock()
    mock_appointment_repo.find_by_professional_and_datetime.return_value = appointment

    mock_client_service = Mock()

    service_appointment = ServiceAppointment(mock_professional_service, mock_working_hours_service, mock_notification_service, mock_client_service, mock_appointment_repo)

    assert not service_appointment.check_availability(professional, datetime_slot)


def test_create_appointment_success():

    professional_service = Mock()
    client_service = Mock()
    working_hours_service = Mock()
    notification_service = Mock()
    appointment_repo = Mock()

    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    professional_service.get_by_id.return_value = professional
    client_service.get_by_id.return_value = Mock()

    appointment_repo.save.return_value = 100

    service = ServiceAppointment(
        professional_service=professional_service,
        client_service=client_service,
        working_hours_service=working_hours_service,
        notification_service=notification_service,
        repo=appointment_repo
    )

    service.check_availability = Mock(return_value=True)

    appointment = service.create_appointment(
        professional_id=26,
        client_id=1,
        datetime_slot=datetime(2030, 5, 18, 10, 0)
    )

    assert appointment.id == 100
    assert appointment.professional_id == 1
    assert appointment.client_id == 1
    assert appointment.state == AppointmentState.PENDING

    appointment_repo.save.assert_called_once()
    notification_service.send_confirmation.assert_called_once()


def test_create_appointment_raises_exception_when_not_available():

    professional_service = Mock()
    client_service = Mock()
    working_hours_service = Mock()
    notification_service = Mock()
    appointment_repo = Mock()

    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9,0), time(13,0)),
            WorkingHours("Miercoles", time(10,0), time(16,0)),
        ],
        default_duration_minutes=30
    )

    professional_service.get_by_id.return_value = professional
    client_service.get_by_id.return_value = Mock()

    service = ServiceAppointment(
        professional_service=professional_service,
        client_service=client_service,
        working_hours_service=working_hours_service,
        notification_service=notification_service,
        repo=appointment_repo
    )

    service.check_availability = Mock(return_value=False)

    with pytest.raises(AvailableException):
        service.create_appointment(
            professional_id=26,
            client_id=1,
            datetime_slot=datetime(2030, 5, 18, 10, 0)
        )

    appointment_repo.save.assert_not_called()
    notification_service.send_confirmation.assert_not_called()


def test_get_by_id_returns_appointment():

    appointment_repo = Mock()

    appointment = Mock()
    appointment.id = 1

    appointment_repo.get_by_id.return_value = appointment

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    result = service.get_by_id(1)

    assert result == appointment


def test_get_by_id_raises_exception_when_appointment_not_exists():

    appointment_repo = Mock()

    appointment_repo.get_by_id.return_value = None

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    with pytest.raises(AvailableException, match="No existe el turno"):
        service.get_by_id(999)


def test_confirm_appointment_success():

    appointment_repo = Mock()

    appointment = Mock()
    appointment.id = 15
    appointment.state = AppointmentState.PENDING

    appointment_repo.get_by_id.return_value = appointment

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    result = service.confirm_appointment(15)

    assert result == appointment

    appointment_repo.get_by_id.assert_called_once_with(15)
    appointment_repo.update_state.assert_called_once_with(
        15,
        AppointmentState.CONFIRMED
    )


def test_confirm_appointment_raises_exception_when_not_pending():

    appointment_repo = Mock()

    appointment = Mock()
    appointment.id = 15
    appointment.state = AppointmentState.CONFIRMED

    appointment_repo.get_by_id.return_value = appointment

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    with pytest.raises(ValidationException, match="Solo se pueden confirmar turnos pendientes"):
        service.confirm_appointment(15)

    appointment_repo.update_state.assert_not_called()


def test_confirm_appointment_raises_exception_when_appointment_not_exists():

    appointment_repo = Mock()
    appointment_repo.get_by_id.return_value = None

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    with pytest.raises(AvailableException, match="No existe el turno"):
        service.confirm_appointment(999)

    appointment_repo.update_state.assert_not_called()


def test_cancel_appointment_success():

    appointment_repo = Mock()

    appointment = Mock()
    appointment.id = 20
    appointment.state = AppointmentState.PENDING

    appointment_repo.get_by_id.return_value = appointment

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    result = service.cancel_appointment(20)

    assert result == appointment

    appointment_repo.get_by_id.assert_called_once_with(20)
    appointment_repo.update_state.assert_called_once_with(
        20,
        AppointmentState.CANCELED
    )


def test_cancel_appointment_raises_exception_when_not_pending():

    appointment_repo = Mock()

    appointment = Mock()
    appointment.id = 20
    appointment.state = AppointmentState.CONFIRMED

    appointment_repo.get_by_id.return_value = appointment

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    with pytest.raises(ValidationException, match="Solo se pueden cancelar turnos pendientes"):
        service.cancel_appointment(20)

    appointment_repo.update_state.assert_not_called()


def test_cancel_appointment_raises_exception_when_appointment_not_exists():

    appointment_repo = Mock()
    appointment_repo.get_by_id.return_value = None

    service = ServiceAppointment(
        professional_service=Mock(),
        client_service=Mock(),
        working_hours_service=Mock(),
        notification_service=Mock(),
        repo=appointment_repo
    )

    with pytest.raises(AvailableException, match="No existe el turno"):
        service.cancel_appointment(999)

    appointment_repo.update_state.assert_not_called()
