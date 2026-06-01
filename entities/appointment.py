class Appointment:
    def __init__(self, id, duration, professional_id, client_id, state):
        self._id = id
        self._duration = duration
        self._professional_id = professional_id
        self._client_id = client_id
        self._state = state