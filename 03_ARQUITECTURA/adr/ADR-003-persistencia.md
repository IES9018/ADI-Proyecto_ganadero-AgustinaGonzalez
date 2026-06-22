# ADR-003: estrategia de persistencia

## Decisión
Se utilizará una base de datos relacional (SQLite en MVP, migrable a PostgreSQL).

## Contexto
Se requiere persistencia estructurada con relaciones claras.

## Consecuencias
- soporte de consultas complejas
- integridad referencial
- facilidad de migración futura