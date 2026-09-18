from pydantic import BaseModel, EmailStr, Field


class ClientRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100) # le indico que el nombre debe tener al menos 1 caracter y como maximo 100
    email: EmailStr # le indico que el email debe ser un email valido
    phone: str = Field(min_length=1, max_length=20)