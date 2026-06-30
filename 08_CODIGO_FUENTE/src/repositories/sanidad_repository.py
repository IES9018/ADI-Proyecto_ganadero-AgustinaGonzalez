import sqlite3

DB_PATH = "ganado.db"


class SanidadRepository:

    def __init__(self):
        self._crear_tabla()

    def _crear_tabla(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS eventos_sanitarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id INTEGER,
                tipo_evento TEXT,
                descripcion TEXT,
                fecha TEXT
            )
        """)

        conn.commit()
        conn.close()

    def crear_evento(self, animal_id, data):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO eventos_sanitarios (animal_id, tipo_evento, descripcion, fecha)
            VALUES (?, ?, ?, ?)
        """, (
            animal_id,
            data["tipo_evento"],
            data["descripcion"],
            data["fecha"]
        ))

        conn.commit()
        conn.close()

        return {"mensaje": "evento creado"}

    def listar_por_animal(self, animal_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, animal_id, tipo_evento, descripcion, fecha
            FROM eventos_sanitarios
            WHERE animal_id = ?
        """, (animal_id,))

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": r[0],
                "animal_id": r[1],
                "tipo_evento": r[2],
                "descripcion": r[3],
                "fecha": r[4]
            }
            for r in rows
        ]

    def eliminar_evento(self, evento_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM eventos_sanitarios WHERE id = ?", (evento_id,))

        conn.commit()
        conn.close()

        return {"mensaje": "evento eliminado"}