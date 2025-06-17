# scripts/nutri_db.py

import mysql.connector

# ✅ Configura tus credenciales MySQL
DB_CONFIG = {
    "host": "localhost",
    "user": "tu_usuario_mysql",
    "password": "tu_contraseña",
    "database": "nutricion"
}

def conectar():
    """Establece conexión con la base de datos."""
    return mysql.connector.connect(**DB_CONFIG)

def insertar_alimento(nombre, kcal, proteinas, carbohidratos, grasas, origen='excel'):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO alimentos (nombre, kcal_per_100g, proteinas, carbohidratos, grasas, origen)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, kcal, proteinas, carbohidratos, grasas, origen))
    conn.commit()
    alimento_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return alimento_id

def insertar_micronutriente(alimento_id, nombre, cantidad_mg):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO micronutrientes (alimento_id, nombre, cantidad_mg)
        VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (alimento_id, nombre, cantidad_mg))
    conn.commit()
    cursor.close()
    conn.close()

def obtener_alimento(nombre):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alimentos WHERE nombre = %s", (nombre,))
    alimento = cursor.fetchone()
    cursor.close()
    conn.close()
    return alimento

def obtener_micros(alimento_id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT nombre, cantidad_mg FROM micronutrientes WHERE alimento_id = %s", (alimento_id,))
    micros = cursor.fetchall()
    cursor.close()
    conn.close()
    return micros
