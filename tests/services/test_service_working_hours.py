from datetime import datetime, time

from src.entities.working_hours import WorkingHours
from src.services.working_hours.service_working_hours import ServiceWorkingHours


def test_check_working_hours_returns_true_when_slot_is_within_working_hours():
    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(14, 0), time(18, 0)),
        WorkingHours("Martes", time(9, 0), time(13, 0)),
        WorkingHours("Miércoles", time(10, 0), time(16, 0)),
    ]


    datetime_slot = datetime(2026, 5, 18, 10, 0)

    service = ServiceWorkingHours()

    assert service.is_within_schedule(working_hours,datetime_slot, 30)

def test_appointment_fits_completely_inside_working_hours():
    working_hours = [
        WorkingHours(
            day_of_week="Lunes",
            start_time=time(9, 0),
            end_time=time(18, 0)
        )
    ]

    datetime_slot = datetime(2026, 8, 10, 17, 0)

    service = ServiceWorkingHours()
    result = service.is_within_schedule(
        working_hours,
        datetime_slot,
        60
    )

    assert result is True


def test_appointment_ending_exactly_at_working_hours_returns_true():
    working_hours = [
        WorkingHours(
            day_of_week="Lunes",
            start_time=time(9, 0),
            end_time=time(18, 0)
        )
    ]

    datetime_slot = datetime(2026, 8, 10, 17, 0)

    service = ServiceWorkingHours()
    result = service.is_within_schedule(
        working_hours,
        datetime_slot,
        60
    )

    assert result is True

def test_check_working_hours_returns_false_when_slot_is_out_working_hours():
    working_hours = [
        WorkingHours("Lunes", time(9, 0), time(12, 0)),
        WorkingHours("Lunes", time(14, 0), time(18, 0)),
        WorkingHours("Martes", time(9, 0), time(13, 0)),
        WorkingHours("Miércoles", time(10, 0), time(16, 0)),
    ]

    datetime_slot = datetime(2026, 5, 18, 13, 30)

    service = ServiceWorkingHours()

    assert not service.is_within_schedule(working_hours, datetime_slot, 30)



def test_appointment_does_not_fit_completely_inside_working_hours():
    working_hours = [
        WorkingHours(
            day_of_week="Lunes",
            start_time=time(9, 0),
            end_time=time(18, 0)
        )
    ]

    datetime_slot = datetime(2026, 8, 10, 17, 30)

    service = ServiceWorkingHours()
    result = service.is_within_schedule(
        working_hours,
        datetime_slot,
        60
    )

    assert result is False


def test_appointment_starting_before_working_hours_returns_false():
    working_hours = [
        WorkingHours(
            day_of_week="Lunes",
            start_time=time(9, 0),
            end_time=time(18, 0)
        )
    ]

    datetime_slot = datetime(2026, 8, 10, 8, 30)

    service = ServiceWorkingHours()
    result = service.is_within_schedule(
        working_hours,
        datetime_slot,
        30
    )

    assert result is False