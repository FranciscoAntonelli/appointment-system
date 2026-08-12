from src.dependencies.dependency_database import get_connection
from src.dependencies.dependency_notification_service import get_notification_service
from src.dependencies.dependency_professional_service import get_professional_service
from src.dependencies.dependency_working_hours_service import get_working_hours_service
from src.dependencies.dependency_client_service import get_client_service
from src.services.appointment.service_appointment import ServiceAppointment
from src.repositories.appointment.postgres_appointment_repository import PostgresAppointmentRepository

# funcion de dependencia de fastapi. Arma todas las dependencias necesarias para crear un service appointment

def get_appointment_service():

    connection = get_connection()

    appointment_repo = PostgresAppointmentRepository(connection)

    return ServiceAppointment(
        professional_service=get_professional_service(),
        working_hours_service=get_working_hours_service(),
        notification_service=get_notification_service(),
        client_service=get_client_service(),
        repo=appointment_repo
    )