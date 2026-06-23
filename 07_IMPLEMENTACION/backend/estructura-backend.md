# Estructura backend – Ganadapp

## 1. Objetivo

Definir cómo se organizará el código fuente del backend.

## 2. Estructura propuesta

src/
├── dominio/
│   ├── entidades/
│   ├── value_objects/
│   └── servicios/
│
├── aplicacion/
│   ├── casos_de_uso/
│
├── infraestructura/
│   ├── persistencia/
│   └── repositorios/
│
├── presentacion/
│   ├── api/
│   └── rutas/
│
└── main.py


## 3. Reglas

- Dominio independiente de frameworks
- Aplicación orquesta lógica
- Infraestructura implementa persistencia
- Presentación expone API