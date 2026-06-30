from fastapi import APIRouter
from services.animal_service import AnimalService

router = APIRouter()
service = AnimalService()


@router.post("/api/animales")
def crear_animal(animal: dict):
    return service.crear_animal(animal)


@router.get("/api/animales")
def listar_animales():
    return service.listar_animales()


@router.delete("/api/animales/{id}")
def eliminar_animal(animal_id: int):
    return service.eliminar_animal(animal_id)


@router.put("/api/animales/{id}")
def actualizar_animal(animal_id: int, animal: dict):
    return service.actualizar_animal(animal_id, animal)