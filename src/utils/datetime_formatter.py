from src.enums.days_of_week import DaysOfWeek


class DateTimeFormatter:

    DAYS_WEEK = [
        DaysOfWeek.LUNES,
        DaysOfWeek.MARTES,
        DaysOfWeek.MIERCOLES,
        DaysOfWeek.JUEVES,
        DaysOfWeek.VIERNES,
        DaysOfWeek.SABADO,
        DaysOfWeek.DOMINGO
    ]

    @staticmethod
    def get_day_name(datetime_slot):
        return DateTimeFormatter.DAYS_WEEK[
            datetime_slot.weekday()
        ].value

    @staticmethod
    def get_time(datetime_slot):
        return datetime_slot.time()