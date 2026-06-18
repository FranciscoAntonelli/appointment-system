class Professional:
    def __init__(self, id, name, specialty, working_hours, default_duration_minutes):
        self._id = id
        self._name = name
        self._specialty = specialty
        self._working_hours = working_hours
        self._default_duration_minutes = default_duration_minutes


    @property
    def id(self):
        return self._id
    
    @property
    def working_hours(self):
        return self._working_hours
    
    @property
    def name(self):
        return self._name
    
    @property
    def duration(self):
        return self._default_duration_minutes
    

    @property
    def specialty(self):
        return self._specialty 