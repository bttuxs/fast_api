from ..schema import SaludosSchema
from ..repository.SaludosRepository import SaludosRepository
from sqlalchemy.orm import Session
from typing import List


class SaludosController:

    def getSaludos(self, db: Session) -> List[SaludosSchema.BaseModel]:
        return SaludosRepository().getSaludos(db)

    def CrearSaludo(self, data: SaludosSchema.SaludosCrear, db: Session) -> SaludosSchema.BaseModel:
        return SaludosRepository().crearSaludo(db, data)
