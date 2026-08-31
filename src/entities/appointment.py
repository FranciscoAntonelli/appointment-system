class Appointment:
    def __init__(self, id, duration, professional_id, datetime_slot, client_id, state):
        self._id = id
        self._duration = duration
        self._professional_id = professional_id
        self._datetime_slot = datetime_slot
        self._client_id = client_id
        self._state = state


    def set_id(self, appointment_id):
        self._id = appointment_id

    def set_state(self, state):
        self._state = state


    @property
    def id(self):
        return self._id

    @property
    def datetime_slot(self):
        return self._datetime_slot
    
    @property
    def duration(self):
        return self._duration
    
    @property
    def professional_id(self):
        return self._professional_id
    
    @property
    def client_id(self):
        return self._client_id
    
    @property
    def state(self):
        return self._state
    
