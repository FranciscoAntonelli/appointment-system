from pydantic import BaseModel


class ClientRequest(BaseModel):
    name: str
    email: str
    phone: str