# Arquitectura Backend – Ganadapp

## 1. Enfoque

Se implementa arquitectura hexagonal (clean architecture ligera).


## 2. Capas

### Dominio
- entidades
- reglas de negocio
- value objects

### Aplicación
- casos de uso
- coordinación de procesos

### Infraestructura
- base de datos
- repositorios
- adaptadores externos

### Presentación
- API REST (FastAPI)



## 3. Flujo de ejecución

cliente → API → casos de uso → dominio → repositorio → base de datos