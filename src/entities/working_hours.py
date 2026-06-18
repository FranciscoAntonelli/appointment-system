class WorkingHours:
    def __init__(self, day_of_week, start_time, end_time):
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time


    @property
    def day_of_week(self):
        return self._day_of_week

    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time