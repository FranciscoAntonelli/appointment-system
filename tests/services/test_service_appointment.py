from unittest.mock import Mock

import pytest

from src.exceptions.not_found_exception import NotFoundException
from src.exceptions.validation_exception import ValidationException
from src.exceptions.conflict_exception import ConflictException
from src.entities.working_hours import WorkingHours
from src.entities.appointment import Appointment
from src.entities.professional import Professional
from src.services.appointment.service_appointment import ServiceAppointment
from src.enums.appointment_state import AppointmentState
from datetime import datetime, time


@pytest.fixture # prepara un objeto Professional para usar en los tests
def professional():
    return Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours=[
            WorkingHours("Lunes", time(9, 0), time(12, 0)),
            WorkingHours("Lunes", time(14, 0), time(18, 0)),
            WorkingHours("Martes", time(9, 0), time(13, 0)),
            WorkingHours("Miércoles", time(10, 0), time(16, 0)),
        ],
        default_duration_minutes=30
    )


@pytest.fixture
def service_appointment():
    professional_service = Mock()
    client_service = Mock()
    working_hours_service = Mock()
    notification_service = Mock()
    appointment_repo = Mock()

    working_hours_service.is_within_schedule.return_value = True

    service = ServiceAppointment(
        professional_service=professional_service,
        client_service=client_service,
        working_hours_service=working_hours_service,
        notification_service=notification_service,
        repo=appointment_repo
    )

    return service, appointment_repo


@pytest.fixture
def appointment_dependencies():
    professional_service = Mock()
    client_service = Mock()
    working_hours_service = Mock()
    notification_service = Mock()
    appointment_repo = Mock()

    working_hours_service.is_within_schedule.return_value = True

    service = ServiceAppointment(
        professional_service=professional_service,
        client_service=client_service,
        working_hours_service=working_hours_service,
        notification_service=notification_service,
        repo=appointment_repo
    )

    return service, appointment_repo, working_hours_service

# --- tests sin errores ---

def test_check_availability_returns_true_when_is_no_appointment(professional, appointment_dependencies):
    service, appointment_repo, working_hours_service = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    appointment_repo.find_conflicting_appointment.return_value = None

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is True

def test_check_availability_returns_true_when_slot_is_canceled(professional, appointment_dependencies):
    service, appointment_repo, working_hours_service = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.CANCELED
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment 

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is True


def test_check_availability_returns_true_when_slot_is_completed(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 15)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.COMPLETED
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is True


# --- tests de errores ---

def test_check_availability_returns_false_when_slot_is_outside_working_hours(professional, appointment_dependencies):
    service, appointment_repo, working_hours_service = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    working_hours_service.is_within_schedule.return_value = False
    result = service.check_availability(
            professional,
            datetime_slot,
            30
        )

    assert result is False
    appointment_repo.find_conflicting_appointment.assert_not_called()



def test_check_availability_returns_false_when_slot_is_busy(professional, appointment_dependencies):
    service, appointment_repo, working_hours_service = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
            professional,
            datetime_slot,
            30
        )

    assert result is False


def test_create_appointment_success(professional):

    professional_service = Mock()
    client_service = Mock()
    working_hours_service = Mock()
    notification_service = Mock()
    appointment_repo = Mock()

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
            WorkingHours("Miércoles", time(10,0), time(16,0)),
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

    with pytest.raises(ConflictException):
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

    with pytest.raises(NotFoundException, match="No existe el turno"):
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

    with pytest.raises(NotFoundException, match="No existe el turno"):
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

    with pytest.raises(NotFoundException, match="No existe el turno"):
        service.cancel_appointment(999)

    appointment_repo.update_state.assert_not_called()



def test_check_availability_returns_false_when_slot_overlaps_at_start(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 15)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is False

    appointment_repo.find_conflicting_appointment.assert_called_once_with(
        1,
        datetime(2026, 5, 18, 10, 15),
        datetime(2026, 5, 18, 10, 45)
    )


def test_check_availability_returns_false_when_slot_overlaps_at_end(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 15),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is False

    appointment_repo.find_conflicting_appointment.assert_called_once_with(
        1,
        datetime(2026, 5, 18, 10, 0),
        datetime(2026, 5, 18, 10, 30)
    )



def test_check_availability_returns_false_when_new_slot_contains_existing(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 0)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=15,
        datetime_slot=datetime(2026, 5, 18, 10, 15),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
        professional,
        datetime_slot,
        60
    )

    assert result is False

    appointment_repo.find_conflicting_appointment.assert_called_once_with(
        1,
        datetime(2026, 5, 18, 10, 0),
        datetime(2026, 5, 18, 11, 0)
    )



def test_check_availability_returns_false_when_existing_slot_contains_new(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 15)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=60,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = appointment

    result = service.check_availability(
        professional,
        datetime_slot,
        15
    )

    assert result is False

    appointment_repo.find_conflicting_appointment.assert_called_once_with(
        1,
        datetime(2026, 5, 18, 10, 15),
        datetime(2026, 5, 18, 10, 30)
    )



def test_check_availability_returns_true_when_slots_are_consecutive(
    professional,
    appointment_dependencies
):
    service, appointment_repo, _ = appointment_dependencies

    datetime_slot = datetime(2026, 5, 18, 10, 30)

    appointment = Appointment(
        id=1,
        professional_id=1,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=10,
        state=AppointmentState.PENDING
    )

    appointment_repo.find_conflicting_appointment.return_value = None

    result = service.check_availability(
        professional,
        datetime_slot,
        30
    )

    assert result is True

    appointment_repo.find_conflicting_appointment.assert_called_once_with(
        1,
        datetime(2026, 5, 18, 10, 30),
        datetime(2026, 5, 18, 11, 0)
    )