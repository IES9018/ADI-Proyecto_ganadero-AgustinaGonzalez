# Casos de Uso – Sistema Ganadapp

## 1. Visión general

Este documento describe los casos de uso funcionales del sistema de gestión ganadera, modelando las interacciones entre usuarios y el sistema.


## 2. Actores

- productor ganadero
- personal de campo



## 3. Casos de uso

### CU-01: gestionar ganado

Actor principal: productor / personal de campo

Descripción:
Permite registrar, actualizar y consultar información de animales.

Flujo principal:
1. usuario accede al sistema
2. selecciona “gestión de ganado”
3. registra o consulta animal
4. sistema almacena o devuelve datos

Flujos alternativos:
- animal ya existe → se actualiza información
- datos incompletos → sistema solicita corrección



### CU-02: Registrar evento sanitario

Actor principal: personal de campo

Descripción:
Registra vacunaciones, tratamientos y movimientos.

Flujo principal:
1. seleccionar animal
2. ingresar evento
3. guardar información
4. sistema actualiza historial

Excepciones:
- animal inexistente → error
- datos inválidos → rechazo



### CU-03: Consultar trazabilidad

Actor principal: productor

Descripción:
Consulta historial completo de un animal.



### CU-04: Gestionar stock

Actor principal: productor / personal de campo

Descripción:
Registro y actualización de insumos.


### CU-05: Generar alertas

Actor principal: sistema

Descripción:
Generación automática de alertas por stock o sanidad.



### CU-06: Autenticación

Actor principal: usuario

Descripción:
Control de acceso por rol.