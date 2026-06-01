from state.state import State


class CanceledState(State):
    def __init__(self):
        self._appointment = None

    def set_appointment(self, appointment):
        self._appointment = appointment

    def blocks_schedule(self):
        return False