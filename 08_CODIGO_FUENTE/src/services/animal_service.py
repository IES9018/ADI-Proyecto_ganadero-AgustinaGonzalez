from repositories.animal_repository import AnimalRepository


class AnimalService:

    def __init__(self):
        self.repo = AnimalRepository()

    def crear_animal(self, data):
        return self.repo.crear(data)

    def listar_animales(self):
        return self.repo.listar()

    def eliminar_animal(self, animal_id: int):
        return self.repo.eliminar(animal_id)

    def actualizar_animal(self, animal_id: int, data):
        return self.repo.actualizar(animal_id, data)