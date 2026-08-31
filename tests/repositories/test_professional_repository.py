from datetime import time

from src.entities.professional import Professional
from src.entities.working_hours import WorkingHours
from src.repositories.professional.postgres_professional_repository import PostgresProfessionalRepository


def test_save_sucefully(db):
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

    repo = PostgresProfessionalRepository(db)

    professional_id = repo.save(professional)

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM professionals WHERE id = %s",
        (professional_id,) 
    )

    row = cursor.fetchone()
    cursor.close()

    assert row is not None
    assert row[1] == professional.name
    assert row[2] == professional.specialty


def test_get_by_id_returns_professional(professional_repo, professional):

    result = professional_repo.get_by_id(professional.id)

    assert result is not None


def test_get_by_id_returns_none_when_professional_not_exists(repo):

    result = repo.get_by_id(999999)

    assert result is None


def test_get_by_id_loads_working_hours(professional_repo, professional):

    result = professional_repo.get_by_id(professional.id)

    assert len(result.working_hours) > 0