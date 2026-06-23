from infraestructura.persistencia.base import Base
from infraestructura.persistencia.database import engine

# importar modelos
from infraestructura.persistencia.models.animal_model import AnimalModel
from infraestructura.persistencia.models.evento_sanitario_model import EventoSanitarioModel
from infraestructura.persistencia.models.insumo_stock_model import InsumoStockModel
from infraestructura.persistencia.models.productor_model import ProductorModel
from infraestructura.persistencia.models.personal_campo_model import PersonalCampoModel


def crear_base_de_datos():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    crear_base_de_datos()