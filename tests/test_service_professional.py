from datetime import datetime
from unittest.mock import Mock
import pytest
from entities.professional import Professional
from exceptions.professional_exception import ProfessionalException
from services.professional.service_professional import ServiceProfessional


def test_get_by_id_returns_true_when_find():
    professional_id = 1

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

    mock_repository_professional = Mock()
    mock_repository_professional.get_by_id.return_value = professional

    service_professional = ServiceProfessional(mock_repository_professional)
    professional = service_professional.get_by_id(professional_id)
    assert professional.id == professional_id

def test_get_by_id_returns_true_when_not_professional_exist():
    professional_id = None
    
    mock_repository_professional = Mock()
    service_professional = ServiceProfessional(mock_repository_professional)

    with pytest.raises(ProfessionalException):
        service_professional.get_by_id(professional_id)

def test_get_by_id_returns_trow_error_when_not_find():
    professional_id = 1

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

    mock_repository_professional = Mock()
    mock_repository_professional.get_by_id.return_value = None

    service_professional = ServiceProfessional(mock_repository_professional)
    with pytest.raises(ProfessionalException):
        service_professional.get_by_id(professional_id)


def test_check_working_hours_returns_true_when_slot_is_within_working_hours():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "Lunes": ["09:00-12:00", "14:00-18:00"],
            "Martes": ["09:00-13:00"],
            "Miercoles": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 10, 0
    )

    mock_repository_professional = Mock()
    service_professional = ServiceProfessional(mock_repository_professional)

    assert service_professional.check_working_hours(professional, datetime_slot)


def test_check_working_hours_returns_false_when_slot_is_out_working_hours():
    professional = Professional(
        id=1,
        name="Dr. Juan Pérez",
        specialty="Dermatology",
        working_hours={
            "Lunes": ["09:00-12:00", "14:00-18:00"],
            "Martes": ["09:00-13:00"],
            "Miercoles": ["10:00-16:00"]
        },
        default_duration_minutes=30
    )

    datetime_slot = datetime(
        2026, 5, 18, 13, 30
    )

    mock_repository_professional = Mock()
    service_professional = ServiceProfessional(mock_repository_professional)

    assert not service_professional.check_working_hours(professional, datetime_slot)