from datetime import datetime

from exceptions.professional_exception import ProfessionalException
from services.professional.i_service_professinal import IServiceProfessional


class ServiceProfessional(IServiceProfessional):
    def __init__(self, repo):
        self._repo = repo

    def _validate_name(self, name):
        pass

    def _validate_working_hours(self, working_hours):
        pass

    def _validate_duration(self, duration):
        pass

    def create_professional(self, professional):
        
        self._repo.save(professional)
    
    def get_by_id(self, professional_id):
        if not professional_id:
            raise ProfessionalException("No hay ningun profesional seleccionado")

        professional = self._repo.get_by_id(professional_id)
        if not professional:
            raise ProfessionalException("No se encuentra ese profesional en la base de datos")

        return professional
        
    
    def check_working_hours(self, professional, datetime_slot):
        days_week = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        day_number = datetime_slot.weekday() # devuelve indice del dia del date
        day_name = days_week[day_number] # devuelve nombre el dia

        slot_time = datetime_slot.time() #devuelve la hora del date

        if day_name in professional.working_hours:
            for fringe in professional.working_hours[day_name]: #recorro la lista de franjas horarias de ese dia
                text_home, text_end = fringe.split("-") # 09:00-12:00" se separa en text_home="09:00" y text_end="12:00"

                start_time = datetime.strptime(text_home, "%H:%M").time() #convierto estos textos a objeto date horas para comparar
                end_time = datetime.strptime(text_end, "%H:%M").time()

                if start_time <= slot_time <= end_time: #evaluo si la hora q quiere el usuario cae dentro del rango especifico 
                    return True
                
        return False




        


        