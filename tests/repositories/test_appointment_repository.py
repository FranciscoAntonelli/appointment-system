from datetime import datetime

import pytest
from src.entities.appointment import Appointment
from src.enums.appointment_state import AppointmentState

def test_save_sucefully(repo, db, professional_id, client_id):

    appointment = Appointment(
        id=None,
        professional_id=professional_id,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=client_id,
        state=AppointmentState.PENDING
    )

    appointment_id = repo.save(appointment) 

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM appointments WHERE id = %s",
        (appointment_id,) #se pone, para indicar q es tupla (la bd necesita parametros tupla)
    )

    row = cursor.fetchone()
    cursor.close()

    assert row is not None
    assert row[1] == appointment.professional_id
    assert row[2] == appointment.client_id


def test_save_returns_error_when_sql_restriction_not_respected(repo, client_id):

    appointment = Appointment(
        id=None,
        professional_id=None,
        duration=30,
        datetime_slot=datetime(2026, 5, 18, 10, 0),
        client_id=client_id,
        state=AppointmentState.PENDING
    )

    with pytest.raises(Exception):
        repo.save(appointment) 


def test_find_by_professional_and_datetime_with_success(repo, professional_id, client_id, appointment_id):

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    result = repo.find_by_professional_and_datetime(
        professional_id,
        datetime_slot
    )

    assert result is not None


def test_get_by_id_returns_appointment(repo, appointment_id):

    result = repo.get_by_id(appointment_id)

    assert result is not None

def test_get_by_id_returns_none_when_appointment_not_exists(repo):

    result = repo.get_by_id(999999)

    assert result is None