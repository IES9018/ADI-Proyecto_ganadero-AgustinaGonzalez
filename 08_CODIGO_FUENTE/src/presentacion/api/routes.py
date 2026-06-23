from fastapi import APIRouter

router = APIRouter()

@router.get("/animales")
def listar_animales():
    return {"mensaje": "Listado de animales (pendiente implementación)"}

@router.post("/animales")
def crear_animal():
    return {"mensaje": "Crear animal (pendiente implementación)"}