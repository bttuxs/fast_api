from fastapi import APIRouter, Depends
from .schema.SaludosSchema import SaludosCrear, Saludos
from .schema import hello
from .controllers.SaludosController import SaludosController
from typing import List
from sqlalchemy.orm import Session
from conf.database import SessionLocal, engine, Base
Base.metadata.create_all(bind=engine)


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/", response_model=hello.Hello)
async def root():
    return {"message": "Hello World"}


@router.get("/saludos", response_model=List[Saludos],
            summary="Catalogo de saludos", description="Es el listado de saludos existentes")
async def SaludosSchema(bbdd: Session = Depends(get_db)):
    return SaludosController().getSaludos(bbdd)


@router.post("/saludos", response_model=SaludosCrear,
             summary="Creacion de saludo", description="Servicio para la creacion de saludos")
async def saludo(saludo: SaludosCrear, bbdd: Session = Depends(get_db)):
    print(saludo)
    return SaludosController().CrearSaludo(saludo, bbdd)
