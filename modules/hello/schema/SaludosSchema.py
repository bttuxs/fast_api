from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SaludosCrear(BaseModel):
    saludos: str


class Saludos(SaludosCrear):
    id: int
    activo: int
    creado: datetime
    actualizado: Optional[datetime]

    class Config:
        orm_mode = True
