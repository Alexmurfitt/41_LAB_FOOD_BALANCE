import os
import shutil

# Carpetas a crear
carpetas_a_crear = [
    "data/usda",
    "data/documentos",
    "data/sql",
    "data/procesamiento",
    "scripts/ingestion",
    "scripts/processing",
    "scripts/output",
    "scripts/queries",
    "scripts/gestion",
    "scripts/config",
    "scripts/docs"
]

# Archivos a mover
mapeo = {
    "data/usda": "data/Fooddata_usda",
    "data/documentos": [
        "data/api_plan.md",
        "data/estructura_bbdd.md",
        "data/DIETA COMPLETA.xlsx"
    ],
    "data/sql": [
        "data/comidas.sql",
        "data/esquema.sql"
    ],
    "data/procesamiento": "data/nutri_db.py",
    "scripts/ingestion": [
        "scripts/import_usda.py",
        "scripts/import_excel.py"
    ],
    "scripts/processing": [
        "scripts/comidas.py",
        "scripts/perfiles.py",
        "scripts/objetivos.py"
    ],
    "scripts/output": [
        "scripts/exportarpdf.py",
        "scripts/visualizaciones.py"
    ],
    "scripts/queries": [
        "scripts/consultas.py",
        "scripts/CONSULTAS_ALIMENTACION.sql",
        "scripts/consultas_avanzadas.sql"
    ],
    "scripts/gestion": [
        "scripts/alertas.py",
        "scripts/respaldo_restauracion.py"
    ],
    "scripts/config": "scripts/config.py",
    "scripts/docs": [
        "scripts/fludo_datos.md",
        "scripts/notas_migracion.md"
    ]
}

def crear_carpetas():
    for carpeta in carpetas_a_crear:
        os.makedirs(carpeta, exist_ok=True)
        print(f"📁 Carpeta asegurada: {carpeta}")

def mover_archivos():
    for destino, origen in mapeo.items():
        if isinstance(origen, str):
            if os.path.exists(origen):
                print(f"📦 Moviendo {origen} → {destino}/")
                shutil.move(origen, destino)
            else:
                print(f"⚠️ Archivo no encontrado: {origen}")
        elif isinstance(origen, list):
            for archivo in origen:
                if os.path.exists(archivo):
                    print(f"📦 Moviendo {archivo} → {destino}/")
                    shutil.move(archivo, destino)
                else:
                    print(f"⚠️ Archivo no encontrado: {archivo}")

def eliminar_pycache():
    print("🧹 Eliminando carpetas '__pycache__'...")
    for root, dirs, files in os.walk("."):
        for d in dirs:
            if d == "__pycache__":
                path = os.path.join(root, d)
                print(f"🗑️  Borrando: {path}")
                shutil.rmtree(path)

if __name__ == "__main__":
    print("🚀 Iniciando reorganización del proyecto ALIMENTACION...\n")
    crear_carpetas()
    mover_archivos()
    eliminar_pycache()
    print("\n✅ Proyecto organizado a nivel profesional. ¡Listo para crecer! 🌱")


