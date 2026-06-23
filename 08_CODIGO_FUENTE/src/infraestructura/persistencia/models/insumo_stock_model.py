from sqlalchemy import Column, Integer, String, Float

from infraestructura.persistencia.base import Base


class InsumoStockModel(Base):

    __tablename__ = "insumo_stock"

    id_insumo = Column(Integer, primary_key=True)

    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    cantidad_actual = Column(Float, nullable=False)

    unidad_medida = Column(String)

    umbral_minimo = Column(Float)