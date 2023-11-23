import sqlalchemy.sql.functions
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
from conf.database import Base


class SaludosModel(Base):
    __tablename__ = "saludos"

    id = Column("id", Integer, primary_key=True, index=True)
    saludos = Column("saludos", String(250))
    activo = Column(Integer, default=1, nullable=False)
    creado = Column(DateTime(timezone=True), server_default=sqlalchemy.sql.functions.now(), nullable=False)
    actualizado = Column(DateTime(timezone=True), server_default=sqlalchemy.sql.functions.now(), server_onupdate=sqlalchemy.sql.functions.now(), nullable=False)
