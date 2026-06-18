from src.services.working_hours.i_service_working_professional import IServiceWorkingHours
from src.utils.datetime_formatter import DateTimeFormatter

class ServiceWorkingHours(IServiceWorkingHours):

    def is_within_schedule(self, working_hours, datetime_slot):

        day_name = DateTimeFormatter.get_day_name(datetime_slot)
        slot_time = DateTimeFormatter.get_time(datetime_slot)

        for wh in working_hours:
            if wh.day_of_week == day_name:

                if wh.start_time <= slot_time <= wh.end_time: #evaluo si la hora q quiere el usuario cae dentro del rango especifico 
                    return True
                
        return False