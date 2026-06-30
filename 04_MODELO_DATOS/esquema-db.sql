-- =========================================================
-- ESQUEMA BASE DE DATOS - GANADAPP
-- =========================================================

-- TABLA PRODUCTOR
CREATE TABLE productor (
    id_productor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT,
    ubicacion TEXT
);

-- TABLA PERSONAL DE CAMPO
CREATE TABLE personal_campo (
    id_personal INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol_operativo TEXT NOT NULL
);

-- TABLA ANIMAL
CREATE TABLE animal (
    id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_identificacion TEXT UNIQUE NOT NULL,
    especie TEXT NOT NULL,
    raza TEXT,
    edad_aproximada INTEGER,
    estado_sanitario TEXT NOT NULL,
    fecha_registro DATE NOT NULL
);

-- TABLA EVENTO SANITARIO
CREATE TABLE evento_sanitario (
    id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_animal INTEGER NOT NULL,
    tipo_evento TEXT NOT NULL,
    fecha DATE NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
);

-- TABLA INSUMO STOCK
CREATE TABLE insumo_stock (
    id_insumo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    cantidad_actual REAL NOT NULL CHECK (cantidad_actual >= 0),
    unidad_medida TEXT,
    umbral_minimo REAL DEFAULT 0
);

-- INDICES
CREATE INDEX idx_evento_animal ON evento_sanitario(id_animal);
CREATE INDEX idx_animal_codigo ON animal(codigo_identificacion);