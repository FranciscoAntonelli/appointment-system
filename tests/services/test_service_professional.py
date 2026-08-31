from unittest.mock import Mock
import pytest
from src.entities.professional import Professional
from src.exceptions.validation_exception import ValidationException
from src.exceptions.not_found_exception import NotFoundException
from src.services.professional.service_professional import ServiceProfessional
from src.entities.working_hours import WorkingHours
from datetime import time


# ---- create_professional ----

# --- tests sin errores ---

def test_create_professional_works_well():
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

    mock_validator = Mock()

    mock_repository_professional = Mock()
    mock_repository_professional.save.return_value = professional

    service_professional = ServiceProfessional(mock_repository_professional, mock_validator)
    professional_created = service_professional.create_professional(professional)
    assert professional_created ==  professional


def test_create_professional_calls_validator_and_repository():
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

    mock_repo = Mock()
    mock_repo.save.return_value = professional

    mock_validator = Mock()

    service = ServiceProfessional(mock_repo, mock_validator)

    result = service.create_professional(professional)

    mock_validator.validate.assert_called_once_with(professional)

    mock_repo.save.assert_called_once_with(professional)

    assert result == professional


#   ---- get_by_id ----

# --- test sin errores ---

def test_get_by_id_returns_true_when_find():
    professional_id = 1

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

    mock_repository_professional = Mock()
    mock_repository_professional.get_by_id.return_value = professional

    mock_validator = Mock()

    service_professional = ServiceProfessional(mock_repository_professional, mock_validator)
    professional = service_professional.get_by_id(professional_id)
    assert professional.id == professional_id

def test_get_by_id_returns_true_when_not_professional_exist():
    professional_id = None
    
    mock_repository_professional = Mock()
    mock_validator = Mock()
    service_professional = ServiceProfessional(mock_repository_professional, mock_validator)

    with pytest.raises(ValidationException, match="No hay ningun profesional seleccionado"):
        service_professional.get_by_id(professional_id)


#tests de errores

def test_get_by_id_returns_trow_error_when_not_find():
    professional_id = 1

    mock_repository_professional = Mock()
    mock_repository_professional.get_by_id.return_value = None

    mock_validator = Mock()

    service_professional = ServiceProfessional(mock_repository_professional, mock_validator)
    
    with pytest.raises(NotFoundException, match="No existe ese profesional"):
        service_professional.get_by_id(professional_id)
