# scripts/import_excel.py

import pandas as pd
from scripts.nutri_db import insertar_alimento, insertar_micronutriente

# ✅ Ruta del archivo Excel personalizado
EXCEL_PATH = "../data/DIETA COMPLETA.xlsx"

# ✅ Nombre de la hoja a leer (puede ser personalizado si es necesario)
SHEET_NAME = "Alimentos"

def importar_desde_excel():
    try:
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
        print(f"📥 Cargando {len(df)} alimentos desde Excel...")

        for _, row in df.iterrows():
            nombre = row["Nombre"]
            prote = float(row.get("Proteínas", 0))
            carbs = float(row.get("Carbohidratos", 0))
            grasas = float(row.get("Grasas", 0))
            kcal = float(row.get("Kcal", (prote * 4 + carbs * 4 + grasas * 9)))

            alimento_id = insertar_alimento(nombre, kcal, prote, carbs, grasas, origen="excel")

            # Micronutrientes dinámicos: todo lo que no sea nombre/macros lo tratamos como micro
            for columna in row.index:
                if columna not in ["Nombre", "Proteínas", "Carbohidratos", "Grasas", "Kcal"]:
                    valor = row[columna]
                    if pd.notna(valor) and float(valor) > 0:
                        insertar_micronutriente(alimento_id, columna, float(valor))

            print(f"✅ '{nombre}' importado con ID {alimento_id}")

        print("🎉 Importación desde Excel completada.")

    except Exception as e:
        print(f"❌ Error al importar Excel: {e}")


if __name__ == "__main__":
    importar_desde_excel()
