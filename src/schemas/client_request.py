from pydantic import BaseModel, EmailStr


class ClientRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str