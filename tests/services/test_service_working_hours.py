from datetime import datetime, time

from src.entities.working_hours import WorkingHours
from src.services.working_hours.service_working_hours import ServiceWorkingHours


def test_check_working_hours_returns_true_when_slot_is_within_working_hours():
    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(14, 0), time(18, 0)),
        WorkingHours("Martes", time(9, 0), time(13, 0)),
        WorkingHours("Miercoles", time(10, 0), time(16, 0)),
    ]


    datetime_slot = datetime(2026, 5, 18, 10, 0)

    service = ServiceWorkingHours()

    assert service.is_within_schedule(working_hours,datetime_slot)

# --- test de errores ---

def test_check_working_hours_returns_false_when_slot_is_out_working_hours():
    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(14, 0), time(18, 0)),
        WorkingHours("Martes", time(9, 0), time(13, 0)),
        WorkingHours("Miercoles", time(10, 0), time(16, 0)),
    ]

    datetime_slot = datetime(2026, 5, 18, 13, 30)

    service = ServiceWorkingHours()

    assert not service.is_within_schedule(working_hours, datetime_slot)