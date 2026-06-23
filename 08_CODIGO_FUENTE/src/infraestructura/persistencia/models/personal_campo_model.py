from sqlalchemy import Column, Integer, String

from infraestructura.persistencia.base import Base


class PersonalCampoModel(Base):

    __tablename__ = "personal_campo"

    id_personal = Column(Integer, primary_key=True)

    nombre = Column(String, nullable=False)

    rol_operativo = Column(String, nullable=False)