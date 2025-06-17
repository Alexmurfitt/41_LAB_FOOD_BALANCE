# scripts/comidas.py

from scripts.nutri_db import conectar
from datetime import datetime

def registrar_comida(nombre, fecha=None, hora=None):
    if not fecha:
        fecha = datetime.today().date()
    if not hora:
        hora = datetime.now().time()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO comidas (nombre, fecha, hora)
        VALUES (%s, %s, %s)
    """, (nombre, fecha, hora))
    conn.commit()
    comida_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return comida_id

def registrar_alimento_en_comida(comida_id, alimento_id, cantidad_g):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO comida_alimentos (comida_id, alimento_id, cantidad_g)
        VALUES (%s, %s, %s)
    """, (comida_id, alimento_id, cantidad_g))
    conn.commit()
    cursor.close()
    conn.close()

def registrar_comida_interactiva():
    print("\n🍽️ Registro de nueva comida")
    nombre_comida = input("Nombre de la comida (ej. Desayuno): ")
    comida_id = registrar_comida(nombre_comida)
    print(f"🆕 Comida '{nombre_comida}' creada con ID {comida_id}\n")

    while True:
        alimento = input("Nombre del alimento (o 'fin' para terminar): ").strip()
        if alimento.lower() == 'fin':
            break

        cantidad = float(input("Cantidad en gramos: "))

        # Buscar alimento
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id FROM alimentos WHERE nombre = %s", (alimento,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        if not resultado:
            print(f"⚠️ Alimento '{alimento}' no encontrado en base de datos.")
            continue

        alimento_id = resultado['id']
        registrar_alimento_en_comida(comida_id, alimento_id, cantidad)
        print(f"✅ '{alimento}' registrado en la comida con {cantidad}g\n")

    print(f"🎉 Comida '{nombre_comida}' registrada exitosamente.")


if __name__ == "__main__":
    registrar_comida_interactiva()
