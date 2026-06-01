from entities.appointment import Appointment
from exceptions.available_exception import AvailableException
from services.appointment.i_service_appointment import IServiceAppointment
from state.pending_state import PendingState


class ServiceAppointment(IServiceAppointment):
    def __init__(self, professional_service, repo):
        self._professional_service = professional_service
        self._appointment_repo = repo

    def check_availability(self, professional, datetime_slot):
        # comprobar si el datetime_slot esta dentro del rango de working hours con true o false
        if not self._professional_service.check_working_hours(professional, datetime_slot):
            return False
        
        # fijarte si hay un turno ocupado en esa fecha por el profesional
        appointment = self._appointment_repo.find_by_professional_and_datetime(professional.id, datetime_slot)

        # te fijas si el estado esta disponible o no con el state y si existe turno
        if(appointment and appointment._state.blocks_schedule()):
            return False
        
        return True

    def create_appointment(self, professional, client_id, datetime_slot):
        professional = self._professional_service.get_by_id(professional.id)
        duration = professional.default_duration_minutes

        available = self.check_availability(professional, datetime_slot)
        if not available:
            raise AvailableException("No hay turno disponible en esa fecha y hora")

        appointment = Appointment(id=None, professional_id=professional.id, duration=duration, client_id=client_id, state=PendingState())

        self._appointment_repo.save(appointment)

        return appointment