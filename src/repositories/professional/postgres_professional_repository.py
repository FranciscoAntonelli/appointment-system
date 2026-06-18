from src.entities.working_hours import WorkingHours
from src.entities.professional import Professional
from src.repositories.professional.professional_repository import ProfessionalRepository


class PostgresProfessionalRepository(ProfessionalRepository):

    def __init__(self, connection):
        super().__init__(connection)

    def save(self, professional):

        cursor = None
        
        try:

            cursor = self._connection.cursor()

            cursor.execute(
                """
                INSERT INTO professionals (name, specialty, default_duration_minutes)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (professional.name, professional.specialty, professional.duration)
            )

            professional_id = cursor.fetchone()[0]

            for wh in professional.working_hours:

                cursor.execute(
                    """
                    INSERT INTO working_hours (professional_id, day_of_week, start_time, end_time)
                    VALUES (%s, %s, %s, %s) 
                    """,
                    (professional_id, wh.day_of_week, wh.start_time, wh.end_time)
                )
            
            self._connection.commit()

            return professional_id
        
        except Exception:
            self._connection.rollback()
            raise

        finally:
            if cursor:
                cursor.close()


    def get_by_id(self, professional_id):

        cursor = None

        try:
            cursor = self._connection.cursor()

            cursor.execute(
                """
                SELECT id, name, specialty, default_duration_minutes
                FROM professionals
                WHERE id = %s
                """,
                (professional_id,)
            )

            row = cursor.fetchone()

            if not row:
                return None
            
            # Horarios del profesional
            cursor.execute(
                """
                SELECT day_of_week, start_time, end_time
                FROM working_hours
                WHERE professional_id = %s
                """,
                (professional_id,)
            )

            working_hours_rows = cursor.fetchall()

            working_hours = []

            for wh in working_hours_rows:
                working_hours.append(
                    WorkingHours(
                        day_of_week=wh[0],
                        start_time=wh[1],
                        end_time=wh[2]
                    )
                )

            return Professional(
                id=row[0],
                name=row[1],
                specialty=row[2],
                working_hours=working_hours,
                default_duration_minutes=row[3]
            )

        finally:
            if cursor:
                cursor.close()