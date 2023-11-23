from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models.SaludosModel import SaludosModel
from ..schema import SaludosSchema


class SaludosRepository:

    def getSaludos(self, db: Session) -> [SaludosModel]:
        return db.query(SaludosModel).all()

    def crearSaludo(self, db: Session, data: SaludosSchema.SaludosCrear) -> SaludosModel:
        print()
        saludo: SaludosModel = SaludosModel()
        saludo.saludos = data.saludos
        try:
            db.add(saludo)
            db.commit()
            db.refresh(saludo)
            return saludo

        except SQLAlchemyError as e:
            if ('duplicate key value violates unique constraint' in str(e.orig)):
                raise Exception("Error nombre de area ya existe")
            raise Exception("Error en inserccion")
