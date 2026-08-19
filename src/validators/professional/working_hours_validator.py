from src.exceptions.professional_exception import ProfessionalException
from src.validators.validator import Validator

class WorkingHoursValidator(Validator):

    def validate(self, working_hours):
        if not working_hours:
            raise ProfessionalException(
                "Las franjas de horarios están vacías"
            )

        self._validate_days(working_hours)
        self._validate_working_hour_ranges(working_hours)
        self._validate_overlapping_hours(working_hours)

    
    def _validate_days(self, working_hours):
        days_week = [
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo"
        ]

        for wh in working_hours:
            if wh.day_of_week not in days_week:
                raise ProfessionalException("El dia no existe")
            

    def _validate_working_hour_ranges(self, working_hours):

        for wh in working_hours:

            if wh.start_time >= wh.end_time:
                raise ProfessionalException(
                    "La hora de inicio es mayor o igual a la hora de fin"
                )
            
    
    def _validate_overlapping_hours(self, working_hours):

        schedules_by_day = {}

        for wh in working_hours:
            schedules_by_day.setdefault( #si el day of week no existe en el diccionario schedules_by_day
                wh.day_of_week,
                []  #crea lista vacia schedules_by_day[wh.day_of_week] = []
            ).append(wh) #agrega el horario a la lista schedules_by_day[wh.day_of_week].append(wh) 

        for day, schedules in schedules_by_day.items():

            schedules.sort(key=lambda x: x.start_time) #ordena la lista 
            #lambda x es una funcion q retorna x.start_time para no tener q hacer otra funcion get

            for i in range(len(schedules) - 1): #corto una pos antes porq si llego al ultimo indice, intentaria acceder a esa pos y me daria error

                current = schedules[i] 
                next_schedule = schedules[i + 1] 

                if current.end_time > next_schedule.start_time:
                    raise ProfessionalException(
                        f"Hay horarios superpuestos el {day}"
                    )