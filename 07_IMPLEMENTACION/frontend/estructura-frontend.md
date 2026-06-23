# Estructura Frontend – Ganadapp

## 1. Objetivo

Definir la organización del frontend del sistema, asegurando consistencia con la arquitectura hexagonal del backend y la simplicidad operativa del entorno rural.


## 2. Enfoque

El frontend será una interfaz web simple, inicialmente monolítica, con evolución futura posible hacia SPA.

Se prioriza:
- velocidad de carga
- simplicidad de uso
- bajo consumo de recursos
- compatibilidad con dispositivos básicos


## 3. Tecnologías base

- HTML5
- CSS3
- JavaScript vanilla

Evolución futura opcional:
- React o Vue (si el sistema escala)


## 4. Estructura propuesta

frontend/
├── pages/
│   ├── login.html
│   ├── dashboard.html
│   ├── ganado.html
│   ├── stock.html
│   └── eventos.html
│
├── assets/
│   ├── css/
│   ├── js/
│   └── img/
│
└── components/
    ├── navbar.js
    ├── cards.js
    └── forms.js



## 5. Reglas de diseño

- Componentes reutilizables
- Separación clara entre lógica y presentación
- Mínima dependencia externa
- Validaciones básicas en cliente

## 6. Integración con backend

El frontend consume la API REST del backend:

- GET /animales
- POST /eventos
- GET /stock
- GET /trazabilidad/{id}


## 7. Principio clave

El frontend no contiene lógica de negocio, únicamente presentación e interacción.