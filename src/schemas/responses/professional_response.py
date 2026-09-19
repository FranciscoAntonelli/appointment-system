from pydantic import BaseModel, ConfigDict

# el response model es el que se va a devolver al cliente, por eso no tiene validaciones, porque ya se supone que el objeto ya esta creado y validado
class ProfessionalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) # le indico a pydantic que tome los atributos del objeto y los convierta en un diccionario, para poder devolverlo al cliente

    id: int
    name: str
    specialty: str
    default_duration_minutes: int