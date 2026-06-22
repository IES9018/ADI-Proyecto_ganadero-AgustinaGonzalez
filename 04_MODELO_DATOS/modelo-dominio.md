# Modelo de Dominio - GanadApp

## Entidades principales

### Usuario
- id_usuario: int
- nombre: string
- email: string
- rol: string
- contacto: string
- estado_activo: boolean
- ultimo_acceso: datetime

### Productor
- id_productor: int
- nombre: string
- documento: string
- contacto: string
- direccion: string
- estado: string

### Establecimiento
- id_establecimiento: int
- nombre: string
- ubicacion: string
- capacidad: int
- estado: string
- id_productor: int

### Animal
- id_animal: int
- identificador: string
- especie: string
- raza: string
- fecha_nacimiento: date
- estado_sanitario: string
- id_establecimiento: int

### EventoSanitario
- id_evento: int
- tipo: string
- fecha: datetime
- descripcion: string
- dosis: string
- id_animal: int
- id_usuario: int

### StockInsumo
- id_stock: int
- tipo_insumo: string
- cantidad: float
- unidad: string
- ubicacion: string
- id_establecimiento: int

---

## Relaciones

- Un productor tiene muchos establecimientos
- Un establecimiento tiene muchos animales
- Un animal tiene muchos eventos sanitarios
- Un usuario registra eventos sanitarios
- Un establecimiento administra stock

---

## Reglas de negocio

- Todo animal debe pertenecer a un establecimiento válido
- El stock no puede ser negativo
- Cada animal tiene un identificador único
- Todo evento sanitario debe estar asociado a un animal existente
- No se permiten eliminaciones físicas de registros históricos

---

## Diagrama ER

```mermaid
erDiagram

PRODUCTOR ||--o{ ESTABLECIMIENTO : tiene
ESTABLECIMIENTO ||--o{ ANIMAL : contiene
ANIMAL ||--o{ EVENTO_SANITARIO : registra
USUARIO ||--o{ EVENTO_SANITARIO : crea
ESTABLECIMIENTO ||--o{ STOCK_INSUMO : administra

PRODUCTOR {
  int id_productor
  string nombre
  string documento
}

ESTABLECIMIENTO {
  int id_establecimiento
  string nombre
  string ubicacion
}

ANIMAL {
  int id_animal
  string identificador
  string especie
  string raza
}

EVENTO_SANITARIO {
  int id_evento
  string tipo
  datetime fecha
}

STOCK_INSUMO {
  int id_stock
  string tipo_insumo
  float cantidad
}