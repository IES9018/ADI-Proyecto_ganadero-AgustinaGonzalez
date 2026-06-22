# Visión arquitectónica del sistema

## Objetivo

Construir un sistema de gestión ganadera modular para pequeños y medianos productores rurales de Malargüe, orientado a la digitalización de procesos productivos, sanitarios y operativos básicos.

## Enfoque arquitectónico

El sistema se implementa bajo una arquitectura modular monolítica con separación clara de capas:

- capa de presentación (UI)
- capa de aplicación (casos de uso)
- capa de dominio (modelo de negocio)
- capa de infraestructura (persistencia)

## Principios de diseño

- separación de responsabilidades
- bajo acoplamiento entre módulos
- alta cohesión por dominio
- extensibilidad futura por módulos
- trazabilidad completa de eventos del sistema

## Estilo arquitectónico

Se adopta arquitectura hexagonal (puertos y adaptadores), donde:

- el dominio es independiente de frameworks
- la infraestructura es intercambiable
- la lógica de negocio es el núcleo central