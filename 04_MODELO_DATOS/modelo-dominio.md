# Modelo de Dominio – Sistema Ganadapp

## 1. Visión general del dominio

El dominio representa la gestión ganadera orientada a la trazabilidad de animales, eventos sanitarios y control de insumos en establecimientos rurales.

Se modela bajo un enfoque de DDD simplificado, priorizando claridad sobre complejidad técnica.



## 2. Entidades principales

### 2.1 Animal (agregado raíz)

Entidad central del sistema.

Atributos:
- id_animal
- codigo_identificacion
- especie
- raza
- edad_aproximada
- estado_sanitario
- fecha_registro

Reglas:
- cada animal es único dentro del sistema
- todos los eventos se asocian a un animal



### 2.2 EventoSanitario

Representa acciones realizadas sobre un animal.

Atributos:
- id_evento
- tipo_evento (vacunacion, tratamiento, movimiento, control)
- fecha
- descripcion
- id_animal (FK)

Reglas:
- todo evento debe pertenecer a un animal existente
- los eventos son inmutables una vez registrados



### 2.3 InsumoStock

Representa recursos operativos.

Atributos:
- id_insumo
- nombre
- tipo (alimento, medicamento, otro)
- cantidad_actual
- unidad_medida
- umbral_minimo

Reglas:
- no se permite stock negativo
- genera alerta si cantidad < umbral_minimo



### 2.4 Productor

Atributos:
- id_productor
- nombre
- contacto
- ubicacion



### 2.5 PersonalCampo

Atributos:
- id_personal
- nombre
- rol_operativo



## 3. value objects

### 3.1 EstadoSanitario
- sano
- en_tratamiento
- en_observacion
- critico

### 3.2 TipoEvento
- vacunacion
- tratamiento
- movimiento
- control

### 3.3 TipoInsumo
- alimento
- medicamento
- suplemento



## 4. agregados

### agregado: Animal
- Animal (raíz)
- EventoSanitario (colección interna)

### agregado: InsumoStock
- InsumoStock (raíz)



## 5. Relaciones del dominio

- Animal 1 ─── * EventoSanitario
- Productor gestiona múltiples animales (lógico, no directo en dominio MVP)
- PersonalCampo registra eventos



## 6. Reglas de negocio globales

- no existen eventos sin animal asociado
- el stock no puede ser negativo
- todo cambio de estado sanitario debe registrarse como evento
- el sistema mantiene trazabilidad completa por animal