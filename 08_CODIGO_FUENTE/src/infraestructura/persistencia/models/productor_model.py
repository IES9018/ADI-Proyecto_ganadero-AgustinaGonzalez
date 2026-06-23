from sqlalchemy import Column, Integer, String

from infraestructura.persistencia.base import Base


class ProductorModel(Base):

    __tablename__ = "productor"

    id_productor = Column(Integer, primary_key=True)

    nombre = Column(String, nullable=False)

    contacto = Column(String)

    ubicacion = Column(String)