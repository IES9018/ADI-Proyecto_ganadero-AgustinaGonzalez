from sqlalchemy import Column, Integer, String, Date, ForeignKey

from infraestructura.persistencia.base import Base


class EventoSanitarioModel(Base):

    __tablename__ = "evento_sanitario"

    id_evento = Column(Integer, primary_key=True)

    id_animal = Column(
        Integer,
        ForeignKey("animal.id_animal"),
        nullable=False
    )

    tipo_evento = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String)