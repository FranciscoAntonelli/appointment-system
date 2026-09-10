from src.services.working_hours.i_service_working_professional import IServiceWorkingHours
from src.utils.datetime_formatter import DateTimeFormatter
from datetime import datetime, timedelta

class ServiceWorkingHours(IServiceWorkingHours):

    def is_within_schedule(self, working_hours, datetime_slot, duration):

        day_name = DateTimeFormatter.get_day_name(datetime_slot) # obtiene el nombre del dia de la semana a partir del datetime_slot

        end_datetime = (datetime_slot + timedelta(minutes=duration)) # suma la duracion al datetime_slot para obtener el final del turno

        for wh in working_hours:
            if wh.day_of_week == day_name:
                # combina la fecha del datetime_slot con la hora de inicio
                start_datetime = datetime.combine( 
                    datetime_slot.date(),
                    wh.start_time
                )

                # combina la fecha del datetime_slot con la hora de fin
                end_datetime_schedule = datetime.combine(
                    datetime_slot.date(),
                    wh.end_time
                )

                # verifica si el datetime_slot esta dentro del rango de working hours
                if start_datetime <= datetime_slot and end_datetime <= end_datetime_schedule:
                    return True
                
        return False