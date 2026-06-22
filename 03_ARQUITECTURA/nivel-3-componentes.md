Diagrama C4 – Nivel 3: Componentes (Backend)
Propósito

Este diagrama descompone el backend del sistema Ganadapp en componentes internos, mostrando cómo se organizan las responsabilidades dentro de la arquitectura hexagonal.

Contenedor principal: API Backend (FastAPI)
Componentes
Gestión de Ganado

Componente responsable del ciclo de vida de los animales dentro del sistema.

Responsabilidades:

registrar animales
actualizar información de ganado
consultar estado individual o grupal
Gestión de Eventos Sanitarios

Componente encargado de la trazabilidad sanitaria y productiva.

Responsabilidades:

registrar vacunaciones
registrar tratamientos
gestionar movimientos del ganado
mantener historial de eventos
Gestión de Stock

Componente encargado del control de insumos.

Responsabilidades:

registrar alimentos, medicamentos e insumos
actualizar cantidades disponibles
generar alertas de stock bajo
Dominio (Entidades y reglas)

Capa central del sistema.

Responsabilidades:

definir entidades principales (Animal, Evento, Insumo)
aplicar reglas de consistencia
asegurar integridad del modelo
Infraestructura (Persistencia)

Capa de acceso a datos.

Responsabilidades:

implementación de repositorios
conexión con base de datos
traducción entre dominio y almacenamiento
Relaciones principales
Gestión Ganado ───► Dominio ───► Infraestructura ───► Base de Datos
Gestión Eventos ───► Dominio ───► Infraestructura ───► Base de Datos
Gestión Stock ─────► Dominio ───► Infraestructura ───► Base de Datos
Alcance del sistema

El backend es responsable de:

implementar la lógica de negocio del sistema
mantener separación entre dominio e infraestructura
asegurar trazabilidad de eventos ganaderos
gestionar operaciones CRUD sobre entidades principales
soportar evolución futura del sistema sin reestructuración profunda