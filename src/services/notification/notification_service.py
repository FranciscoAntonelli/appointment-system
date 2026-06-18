from src.services.notification.i_notification_service import INotificationService


class NotificationService(INotificationService):

    def send_confirmation(self, appointment, professional):
        print(
            f"Turno confirmado correctamente\n"
            f"Profesional:{professional.name}\n"
            f"Fecha:{appointment.datetime_slot}\n"
            f"Duración: {appointment.duration} minutos")