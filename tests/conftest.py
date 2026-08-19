from datetime import datetime, time
import os

import pytest
from connections.postgres_connection import PostgresConnection
from src.repositories.client.postgres_client_repository import PostgresClientRepository
from src.repositories.professional.postgres_professional_repository import PostgresProfessionalRepository
from src.entities.professional import Professional
from src.entities.working_hours import WorkingHours
from src.enums.appointment_state import AppointmentState
from src.entities.client import Client
from src.repositories.appointment.postgres_appointment_repository import PostgresAppointmentRepository
from dotenv import load_dotenv


@pytest.fixture
def db():
    load_dotenv()

    connection = PostgresConnection(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    ).connect()

    yield connection

    connection.rollback()
    connection.close()

@pytest.fixture()
def repo(db):
    return PostgresAppointmentRepository(db)

@pytest.fixture()
def professional_repo(db):
    return PostgresProfessionalRepository(db)

@pytest.fixture
def professional(professional_repo):

    professional = Professional(
        id=None,
        name="Test",
        specialty="Cardiologia",
        default_duration_minutes=30,
        working_hours=[
            WorkingHours(
                day_of_week="Lunes",
                start_time=time(9, 0),
                end_time=time(17, 0)
            )
        ]
    )

    professional_id = professional_repo.save(professional)

    professional._id = professional_id

    return professional

@pytest.fixture()
def professional_id(db):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO professionals (name, specialty, default_duration_minutes) 
                   VALUES ('Test', 'General', 30)
                   RETURNING id""") #triple comillas = texto largo
    
    prof_id = cursor.fetchone()[0]
    db.commit()
    return prof_id

@pytest.fixture
def client_id(db):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO clients (name, email)
        VALUES ('Test Client', 'test@example.com')
        RETURNING id
    """)

    client_id = cursor.fetchone()[0]
    db.commit()
    return client_id


@pytest.fixture
def working_hours(db, professional_id):
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO working_hours (professional_id, day_of_week, start_time, end_time)
        VALUES (%s, %s, %s, %s)
    """, (
        professional_id,
        "Lunes",
        "09:00:00",
        "18:00:00"
    ))

    db.commit()
    return True


@pytest.fixture
def appointment(db, professional_id, client_id):
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO appointments (
            professional_id,
            client_id,
            datetime_slot,
            state,
            duration    
        )
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (
        professional_id,
        client_id,
        datetime(2026, 5, 18, 10, 0),
        AppointmentState.PENDING.value,
        30
    ))

    appointment_id = cursor.fetchone()[0]
    db.commit()

    return appointment_id

@pytest.fixture
def client_repo(db):
    return PostgresClientRepository(db)


@pytest.fixture
def client(db):

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO clients(name, email, phone)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (
            "Juan Perez",
            "juan@gmail.com",
            "123456789"
        )
    )

    client_id = cursor.fetchone()[0]

    db.commit()
    cursor.close()

    return Client(
        id=client_id,
        name="Juan Perez",
        email="juan@gmail.com",
        phone="123456789"
    )