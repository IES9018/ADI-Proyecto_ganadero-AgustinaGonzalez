import sqlite3

DB_PATH = "ganado.db"


class AnimalRepository:

    def __init__(self):
        self._crear_tabla()

    def _crear_tabla(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS animales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                estado TEXT
            )
        """)

        conn.commit()
        conn.close()

    def crear(self, data):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO animales (codigo, especie, raza, edad, estado)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["codigo"],
            data["especie"],
            data["raza"],
            data["edad"],
            data["estado"]
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "animal creado"}

    def listar(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM animales")
        rows = cursor.fetchall()

        conn.close()

        return [
            {
                "id": r[0],
                "codigo": r[1],
                "especie": r[2],
                "raza": r[3],
                "edad": r[4],
                "estado": r[5]
            }
            for r in rows
        ]

    def eliminar(self, animal_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM animales WHERE id = ?", (animal_id,))

        conn.commit()
        conn.close()

        return {"mensaje": "animal eliminado"}

    def actualizar(self, animal_id, data):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE animales
            SET codigo = ?,
                especie = ?,
                raza = ?,
                edad = ?,
                estado = ?
            WHERE id = ?
        """, (
            data["codigo"],
            data["especie"],
            data["raza"],
            data["edad"],
            data["estado"],
            animal_id
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "animal actualizado"}