Diagrama C4 – Nivel 2: Contenedores
Propósito

Este diagrama describe la estructura interna del sistema Ganadapp, identificando los principales contenedores tecnológicos y su interacción.

Sistema principal: Sistema de Gestión Ganadera (Ganadapp)
Contenedores
Aplicación Web (Frontend)

Interfaz de usuario utilizada por productores y personal de campo para interactuar con el sistema.

Responsabilidades:

visualización de datos
formularios de carga de información
consulta de reportes básicos
interacción con la API
API Backend (FastAPI)

Componente central que expone la lógica del sistema y coordina las operaciones entre frontend, dominio y persistencia.

Responsabilidades:

exponer endpoints REST
aplicar reglas de aplicación
coordinar casos de uso
gestionar autenticación básica
Módulo de Dominio

Núcleo lógico del sistema donde residen las reglas de negocio.

Responsabilidades:

modelar entidades (ganado, eventos, stock)
aplicar reglas de consistencia
gestionar lógica de trazabilidad
Base de Datos (SQLite / PostgreSQL)

Sistema de almacenamiento persistente.

Responsabilidades:

almacenar registros de ganado
almacenar eventos sanitarios y productivos
almacenar stock e insumos
garantizar integridad referencial
Relaciones principales
Usuario
  │
  ▼
Frontend Web
  │
  ▼
API REST (FastAPI)
  │
  ▼
Módulo de Aplicación
  │
  ▼
Módulo de Dominio
  │
  ▼
Base de Datos
Alcance del sistema

El sistema en este nivel es responsable de:

proveer una interfaz web accesible
exponer una API REST estructurada
encapsular reglas de negocio en el dominio
persistir información de forma consistente
mantener separación clara entre capas