class Client:

    def __init__(self, id, name, email, phone):
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone