# ADR-001: Selección de arquitectura monolítica con base de datos relacional (PostgreSQL)

## Contexto

El sistema GanadApp se desarrolla para la gestión ganadera de pequeños y medianos productores de Malargüe, junto con usuarios institucionales en un entorno académico.

Se estima una concurrencia baja a media (10 a 30 usuarios simultáneos) y un volumen moderado de usuarios (20 a 100 productores). El dominio está compuesto por entidades altamente relacionales como productores, ganado, eventos sanitarios y stock.

---

## Decisión

Se adopta una arquitectura monolítica modular con backend único y base de datos relacional PostgreSQL. El sistema se expondrá mediante una API centralizada consumida por aplicaciones web y móvil.

---

## Opciones consideradas

### Opción A: Arquitectura monolítica modular (seleccionada)
Ventajas:
- Menor complejidad de implementación.
- Adecuada para el volumen de usuarios previsto.
- Facilita el desarrollo en contexto académico.
- Integración natural con PostgreSQL.

Desventajas:
- Escalabilidad limitada a largo plazo.
- Riesgo de acoplamiento si no se modulariza correctamente.

---

### Opción B: Arquitectura de microservicios
Ventajas:
- Escalabilidad independiente por servicio.
- Alta flexibilidad tecnológica.

Desventajas:
- Alta complejidad de infraestructura.
- No justificado para la carga del sistema.
- Exceso de overhead para un cuatrimestre académico.

---

## Consecuencias

### Positivas
- Desarrollo más rápido y controlado.
- Consistencia fuerte de datos con PostgreSQL.
- Despliegue simple.
- Adecuado para evolución incremental del sistema.

### Negativas
- Menor escalabilidad horizontal.
- Dependencia fuerte del backend central.
- Posible crecimiento desordenado si no se modulariza correctamente.

### Riesgos
- Acoplamiento entre módulos.
- Posible sobrecarga del backend.
- Evolución futura hacia arquitectura distribuida más compleja.