from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated
class MedecinCreate(BaseModel):
    username: str
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    glucose: float
    bmi: float
    bloodpressure: float
    pedigree: float
