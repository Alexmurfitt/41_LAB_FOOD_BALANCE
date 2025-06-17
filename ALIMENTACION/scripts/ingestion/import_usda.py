import csv
import mysql.connector
from pathlib import Path
from config import DB_CONFIG

# Paths a los CSV
BASE_PATH = Path("../data/FoodData_USDA")
FOOD_CSV = BASE_PATH / "food.csv"
NUTRIENT_CSV = BASE_PATH / "nutrient.csv"
FOOD_NUTRIENT_CSV = BASE_PATH / "food_nutrient.csv"

# Nutrientes que queremos importar (puedes añadir más)
NUTRIENTES_DESEADOS = {
    1003: "proteinas",      # Protein
    1004: "grasas",         # Total lipid (fat)
    1005: "carbohidratos",  # Carbohydrate
    1008: "kcal"            # Energy
}

# 1. Cargar los nutrientes de interés
def cargar_nutrientes_interes():
    return set(NUTRIENTES_DESEADOS.keys())

# 2. Leer y filtrar alimentos
def cargar_alimentos():
    alimentos = {}
    with open(FOOD_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            alimentos[row["fdc_id"]] = row["description"]
    return alimentos

# 3. Leer y agrupar nutrientes por alimento
def cargar_nutrientes_por_alimento(nutrientes_interes):
    datos = {}
    with open(FOOD_NUTRIENT_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            fdc_id = row["fdc_id"]
            nutrient_id = int(row["nutrient_id"])
            if nutrient_id in nutrientes_interes:
                valor = float(row["amount"]) if row["amount"] else 0
                datos.setdefault(fdc_id, {})[nutrient_id] = valor
    return datos

# 4. Insertar alimentos a la base de datos
def importar_alimentos(alimentos, nutrientes_por_alimento):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()

    for fdc_id, nombre in alimentos.items():
        if fdc_id not in nutrientes_por_alimento:
            continue
        nutrientes = nutrientes_por_alimento[fdc_id]

        prote = nutrientes.get(1003, 0)
        grasa = nutrientes.get(1004, 0)
        carbs = nutrientes.get(1005, 0)
        kcal = nutrientes.get(1008, 0)

        try:
            cur.execute("""
                INSERT INTO alimentos (nombre, proteinas, carbohidratos, grasas, kcal)
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, prote, carbs, grasa, kcal))
        except mysql.connector.Error as e:
            print(f"❌ Error al insertar {nombre}: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Alimentos importados con éxito")

# === EJECUCIÓN ===
if __name__ == "__main__":
    nutrientes_interes = cargar_nutrientes_interes()  # Cargar nutrientes que nos interesan
    alimentos = cargar_alimentos()  # Cargar alimentos desde el archivo CSV
    nutrientes_por_alimento = cargar_nutrientes_por_alimento(nutrientes_interes)  # Cargar nutrientes por alimento
    importar_alimentos(alimentos, nutrientes_por_alimento)  # Insertar en la base de datos

