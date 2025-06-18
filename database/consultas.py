# scripts/consultas.py

from scripts.nutri_db import conectar

def resumen_nutricional_por_comida(nombre_comida):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.nombre AS comida, a.nombre AS alimento, ca.cantidad_g,
               a.kcal_per_100g, a.proteinas, a.carbohidratos, a.grasas,
               (a.kcal_per_100g * ca.cantidad_g / 100) AS kcal,
               (a.proteinas * ca.cantidad_g / 100) AS proteinas,
               (a.carbohidratos * ca.cantidad_g / 100) AS carbs,
               (a.grasas * ca.cantidad_g / 100) AS grasas
        FROM comidas c
        JOIN comida_alimentos ca ON c.id = ca.comida_id
        JOIN alimentos a ON ca.alimento_id = a.id
        WHERE c.nombre = %s
    """, (nombre_comida,))

    resultados = cursor.fetchall()
    cursor.close()
    conn.close()

    if not resultados:
        print("❌ Comida no encontrada.")
        return

    print(f"\n📊 Resumen de la comida '{nombre_comida}':\n")
    total_kcal = total_p = total_c = total_g = 0
    for r in resultados:
        print(f"🍽️ {r['alimento']} - {r['cantidad_g']}g: {r['kcal']:.1f} kcal")
        total_kcal += r['kcal']
        total_p += r['proteinas']
        total_c += r['carbohidratos']
        total_g += r['grasas']

    print("\n✅ Totales:")
    print(f"   🔥 Calorías:      {total_kcal:.1f} kcal")
    print(f"   🥩 Proteínas:     {total_p:.1f} g")
    print(f"   🍞 Carbohidratos: {total_c:.1f} g")
    print(f"   🥑 Grasas:        {total_g:.1f} g")

def resumen_diario(fecha):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.nombre AS comida, a.nombre AS alimento, ca.cantidad_g,
               a.kcal_per_100g, a.proteinas, a.carbohidratos, a.grasas,
               (a.kcal_per_100g * ca.cantidad_g / 100) AS kcal,
               (a.proteinas * ca.cantidad_g / 100) AS proteinas,
               (a.carbohidratos * ca.cantidad_g / 100) AS carbs,
               (a.grasas * ca.cantidad_g / 100) AS grasas
        FROM comidas c
        JOIN comida_alimentos ca ON c.id = ca.comida_id
        JOIN alimentos a ON ca.alimento_id = a.id
        WHERE c.fecha = %s
    """, (fecha,))

    resultados = cursor.fetchall()
    cursor.close()
    conn.close()

    if not resultados:
        print("❌ No hay comidas registradas ese día.")
        return

    print(f"\n📆 Resumen del día {fecha}:")
    total_kcal = total_p = total_c = total_g = 0
    for r in resultados:
        total_kcal += r['kcal']
        total_p += r['proteinas']
        total_c += r['carbohidratos']
        total_g += r['grasas']

    print(f"\n🔥 Calorías totales:      {total_kcal:.1f} kcal")
    print(f"🥩 Proteínas totales:     {total_p:.1f} g")
    print(f"🍞 Carbohidratos totales: {total_c:.1f} g")
    print(f"🥑 Grasas totales:        {total_g:.1f} g")
