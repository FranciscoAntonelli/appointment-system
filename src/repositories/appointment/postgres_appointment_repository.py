from src.entities.appointment import Appointment
from src.enums.appointment_state import AppointmentState
from src.repositories.appointment.appointment_repository import AppointmentRepository


class PostgresAppointmentRepository(AppointmentRepository):

    def __init__(self, connection):
        super().__init__(connection)

    def save(self, appointment):

        cursor = None

        try:

            cursor = self._connection.cursor() # permite ejecutar y leer resultados de sql

            cursor.execute( #el returning me devuelve el valor generado por el insert
                """
                INSERT INTO appointments (professional_id, client_id, 
                datetime_slot, duration, state)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
                """,
                (appointment.professional_id, appointment.client_id, 
                appointment.datetime_slot, appointment.duration, appointment.state.value)
            )

            appointment_id = cursor.fetchone()[0] #obtengo el id

            self._connection.commit() #confirma y guarda los cambios en la bd

            return appointment_id
            
        except Exception:
            self._connection.rollback() #deshace los cambios q hice en la bd
            raise #lanza excepcion original

        finally:
            if cursor:
                cursor.close()


    def find_conflicting_appointment(self,professional_id,start_datetime,end_datetime):
        cursor = None

        try:
            cursor = self._connection.cursor()

            # el interval '1 minute' convierte la duracion en minutos a un intervalo de tiempo que se puede sumar a datetime_slot
            cursor.execute( #la consulta pregunta si el turno existente empieza antes del final del nuevo turno y termina despues del inicio del nuevo turno. Si es asi, hay conflicto
                """
                SELECT id,
                    professional_id,
                    client_id,
                    datetime_slot,
                    state,
                    duration
                FROM appointments
                WHERE professional_id = %s
                AND datetime_slot < %s
                AND datetime_slot + (duration * INTERVAL '1 minute') > %s 
                """,
                (
                    professional_id,
                    end_datetime,
                    start_datetime,
                )
            )

            row = cursor.fetchone()

            if not row:
                return None

            return Appointment(
                id=row[0],
                professional_id=row[1],
                client_id=row[2],
                datetime_slot=row[3],
                state=AppointmentState(row[4]),
                duration=row[5]
            )

        finally:
            if cursor:
                cursor.close()


    def get_by_id(self, appointment_id):

        cursor = None

        try:

            cursor = self._connection.cursor()

            cursor.execute(
                """
                SELECT *
                FROM appointments
                WHERE id = %s
                """,
                (appointment_id,)
            )

            row = cursor.fetchone()

            if not row:
                return None

            return Appointment(
                id=row[0],
                professional_id=row[1],
                client_id=row[2],
                datetime_slot=row[3],
                state=AppointmentState(row[4]),
                duration=row[5]
            )

        finally:
            if cursor:
                cursor.close()
            
       
    def update_state(self, appointment_id, state):

        cursor = None

        try:
            cursor = self._connection.cursor()

            cursor.execute("""
                UPDATE appointments
                SET state = %s
                WHERE id = %s
            """, (state.value, appointment_id))

            self._connection.commit()

        except Exception:
            self._connection.rollback()
            raise

        finally:
            if cursor:
                cursor.close()