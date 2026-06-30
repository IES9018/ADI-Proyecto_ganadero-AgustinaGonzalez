1. Pantalla de Login
Objetivo

Iniciar sesión y redirigir según rol.

Wireframe
+----------------------------------+
|        GANADAPP MALARGÜE           |
+----------------------------------+
| Usuario:   [______________]      |
| Contraseña:[______________]      |
|                                  |
|        [ Ingresar ]              |
|                                  |
|  ¿Olvidó su contraseña?          |
+----------------------------------+


Flujo 
```mermaid
sequenceDiagram
actor Usuario
participant UI
participant Sistema

Usuario->>UI: Ingresa credenciales
UI->>Sistema: Validar usuario
Sistema-->>UI: Resultado validación
UI-->>Usuario: Redirección por rol
```

UX
Campos mínimos
Mensajes de error claros
Redirección automática por rol
2. Dashboard (Panel principal)
Objetivo

Visualizar estado general del sistema.

Wireframe
+--------------------------------------+
| LOGO | DASHBOARD | usuario          |
+--------------------------------------+
| MENU | RESUMEN PRINCIPAL            |
|      | - Animales: 120             |
|      | - Vacunas pendientes: 8     |
|      | - Stock crítico: 3          |
|      |                             |
|      | ALERTAS                     |
|      | [Vacunación próxima]       |
|      | [Stock bajo]               |
+--------------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Usuario
participant UI
participant Sistema

Usuario->>UI: Accede al dashboard
UI->>Sistema: Solicitar resumen
Sistema-->>UI: Datos consolidados
UI-->>Usuario: Mostrar panel
```
UX
Información crítica priorizada
Tarjetas simples
Visión rápida del estado general
3. Gestión de Productores
Objetivo

Administrar productores registrados.

Wireframe
+------------------------------+
| PRODUCTORES                 |
+------------------------------+
| [+ Nuevo productor]         |
|                              |
| Nombre | Tel | Localidad    |
|-----------------------------|
| Juan   | xxx | Malargüe    |
| Ana    | xxx | Bardas      |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Admin
participant UI
participant Sistema

Admin->>UI: Accede a productores
UI->>Sistema: Solicitar lista
Sistema-->>UI: Lista productores
Admin->>UI: Crear/editar productor
UI->>Sistema: Guardar cambios
```

4. Gestión de Animales
Objetivo

Administrar animales y su estado sanitario.

Wireframe
+------------------------------+
| ANIMALES                   |
+------------------------------+
| [+ Nuevo animal]            |
|-----------------------------|
| ID | Raza | Estado | Estab. |
|-----------------------------|
| 01 | Angus| Sano   | Campo1 |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Usuario
participant UI
participant Sistema

Usuario->>UI: Accede a animales
UI->>Sistema: Consultar registros
Sistema-->>UI: Lista animales
Usuario->>UI: Registrar animal
UI->>Sistema: Guardar datos
```
UX
Identificación por ID único
Estado visible claramente
5. Vacunación / Sanidad
Objetivo

Registrar y consultar vacunación.

Wireframe
+------------------------------+
| VACUNACIÓN                |
+------------------------------+
| Animal: [_____]             |
| Vacuna: [_____]             |
| Fecha:  [_____]             |
|                              |
| [Registrar]                 |
|-----------------------------|
| Historial                  |
| Animal | Vacuna | Fecha    |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Técnico
participant UI
participant Sistema

Técnico->>UI: Registra vacuna
UI->>Sistema: Guardar vacunación
Sistema-->>UI: Confirmación
UI-->>Técnico: Historial actualizado
```
6. Stock de insumos
Objetivo

Controlar inventario.

Wireframe
+------------------------------+
| STOCK                     |
+------------------------------+
| [+ Nuevo insumo]           |
|-----------------------------|
| Insumo | Cantidad | Estado |
|-----------------------------|
| Vacuna | 10       | OK     |
| Alim   | 2        | BAJO   |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Usuario
participant UI
participant Sistema

Usuario->>UI: Consulta stock
UI->>Sistema: Obtener inventario
Sistema-->>UI: Lista insumos
```
7. Movimientos de ganado
Objetivo

Registrar trazabilidad.

Wireframe
+------------------------------+
| MOVIMIENTOS             |
+------------------------------+
| Animal: [___]              |
| Origen: [___]              |
| Destino:[___]              |
| Fecha:  [___]              |
| [Registrar]               |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Técnico
participant UI
participant Sistema

Técnico->>UI: Registra movimiento
UI->>Sistema: Guardar trazabilidad
Sistema-->>UI: Confirmación
```
8. Reportes
Objetivo

Generar análisis del sistema.

Wireframe
+------------------------------+
| REPORTES                |
+------------------------------+
| [Ganado total]             |
| [Sanidad]                 |
| [Stock]                   |
|                            |
| [Exportar PDF]            |
+------------------------------+
Flujo
```mermaid
sequenceDiagram
actor Admin
participant UI
participant Sistema

Admin->>UI: Solicita reporte
UI->>Sistema: Generar datos
Sistema-->>UI: Reporte listo
```
9. Usuarios y roles
Objetivo

Administrar usuarios del sistema.

Flujo
```mermaid
sequenceDiagram
actor Admin
participant UI
participant Sistema

Admin->>UI: Gestiona usuarios
UI->>Sistema: Crear/editar usuario
Sistema-->>UI: Confirmación
```
10. Configuración del sistema
Objetivo

Configurar parámetros generales.

Flujo
```mermaid
sequenceDiagram
actor Admin
participant UI
participant Sistema

Admin->>UI: Accede a configuración
UI->>Sistema: Obtener parámetros
Admin->>UI: Modifica ajustes
UI->>Sistema: Guardar configuración
```