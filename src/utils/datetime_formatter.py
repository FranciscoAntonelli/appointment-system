from src.enums.days_of_week import DaysOfWeek


class DateTimeFormatter:

    @staticmethod
    def get_day_name(datetime_slot):
        days = list(DaysOfWeek)
        return days[datetime_slot.weekday()].value

    @staticmethod
    def get_time(datetime_slot):
        return datetime_slot.time()