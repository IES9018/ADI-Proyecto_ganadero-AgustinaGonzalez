from sqlalchemy import Column, Integer, String, Date

from infraestructura.persistencia.base import Base


class AnimalModel(Base):

    __tablename__ = "animal"

    id_animal = Column(Integer, primary_key=True)
    codigo_identificacion = Column(String, unique=True, nullable=False)
    especie = Column(String, nullable=False)
    raza = Column(String)
    edad_aproximada = Column(Integer)
    estado_sanitario = Column(String, nullable=False)
    fecha_registro = Column(Date, nullable=False)