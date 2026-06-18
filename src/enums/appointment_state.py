from enum import Enum

class AppointmentState(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    COMPLETED = "completed"

    def blocks_schedule(self):
        return self in {
            AppointmentState.PENDING,
            AppointmentState.CONFIRMED
        }