from src.dependencies.dependency_database import get_connection
from src.services.professional.service_professional import ServiceProfessional
from src.repositories.professional.postgres_professional_repository import PostgresProfessionalRepository
from src.validators.professional.working_hours_validator import WorkingHoursValidator
from src.validators.professional.professional_validator import ProfessionalValidator


def get_professional_service():

    connection = get_connection()

    professional_repo = PostgresProfessionalRepository(connection)

    working_hours_validator = WorkingHoursValidator()

    professional_validator = ProfessionalValidator(
        working_hours_validator
    )

    return ServiceProfessional(
        professional_repo,
        professional_validator
    )