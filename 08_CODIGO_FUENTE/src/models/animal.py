from dataclasses import dataclass

@dataclass
class Animal:
    id: int | None
    codigo: str
    especie: str
    raza: str
    edad: int
    estado: str