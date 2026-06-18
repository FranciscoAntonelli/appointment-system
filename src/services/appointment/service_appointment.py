from src.entities.appointment import Appointment
from src.exceptions.available_exception import AvailableException
from src.services.appointment.i_service_appointment import IServiceAppointment
from src.enums.appointment_state import AppointmentState
from datetime import datetime


class ServiceAppointment(IServiceAppointment):
    def __init__(self, professional_service, working_hours_service, notification_service, client_service, repo):
        self._professional_service = professional_service
        self._working_hours_service = working_hours_service
        self._notification_service = notification_service
        self._client_service = client_service
        self._appointment_repo = repo

    def check_availability(self, professional, datetime_slot):
        # comprobar si el datetime_slot esta dentro del rango de working hours con true o false
        if not self._working_hours_service.is_within_schedule(professional.working_hours, datetime_slot):
            return False
        
        # fijarte si hay un turno ocupado en esa fecha por el profesional
        appointment = self._appointment_repo.find_by_professional_and_datetime(professional.id, datetime_slot)

        # me fijo si el estado esta disponible o no con el state y si existe turno
        if(appointment and appointment.state.blocks_schedule()):
            return False
        
        return True

    def create_appointment(self, professional_id, client_id, datetime_slot):

        professional = self._professional_service.get_by_id(professional_id)
        duration = professional.duration

        now = datetime.now()

        if datetime_slot < now:
            raise AvailableException("La fecha y hora del turno debe ser futura")

        client = self._client_service.get_by_id(client_id)

        available = self.check_availability(professional, datetime_slot)

        if not available:
            raise AvailableException("No hay turno disponible en esa fecha y hora")

        appointment = Appointment(id=None, professional_id=professional.id, duration=duration, 
                                  datetime_slot=datetime_slot, 
                                  client_id=client_id, state=AppointmentState.PENDING)

        appointment_id = self._appointment_repo.save(appointment)

        appointment.set_id(appointment_id)

        self._notification_service.send_confirmation(appointment, professional)

        return appointment
    
    def get_by_id(self, appointment_id):

        appointment = self._appointment_repo.get_by_id(appointment_id)

        if not appointment:
            raise AvailableException("No existe el turno")

        return appointment
    

    