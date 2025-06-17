# 🍏 NutriApp

**NutriApp** es un sistema avanzado de seguimiento nutricional que permite registrar alimentos, calcular valores nutricionales por cantidad, generar resúmenes diarios y semanales, y visualizar todo desde una interfaz web o línea de comandos.

> Construido con **Python + Flask + MySQL**

---

## ✅ Funcionalidades principales

- Registro de alimentos con macronutrientes y micronutrientes.
- Importación automática desde USDA y Excel.
- Registro de comidas con múltiples alimentos y cantidades.
- Cálculo automático de macros y micros por comida y por día.
- Visualización web de resúmenes diarios.
- CLI interactiva para consultas avanzadas desde terminal.
- Exportación a PDF y análisis de progreso semanal.

---

## 🧱 Estructura del proyecto

```bash
ALIMENTACION/
├── app/                    # Aplicación Flask
│   ├── app.py
│   ├── cli.py
│   ├── __init__.py
│   └── templates/
│       ├── alimento_form.html
│       ├── index.html
│       └── resumen.html
│
├── data/                   # Datos, estructura y documentos
│   ├── api_plan.md
│   ├── comidas.sql
│   ├── DIETA COMPLETA.xlsx
│   ├── esquema.sql
│   ├── estructura_bbdd.md
│   ├── Fooddata_usda/      # Dataset completo USDA (más de 30 archivos)
│   ├── nutri_db.py
│   └── requirements.txt
│
├── scripts/                # Scripts funcionales
│   ├── alertas.py
│   ├── ALIMENTACION.sql
│   ├── ASIG_ALIM_CANT.py
│   ├── ASIG_ALIM.py
│   ├── comidas.py
│   ├── config.py
│   ├── CONSULTAS_ALIMENTACION.sql
│   ├── consultas.py
│   ├── consultas_avanzadas.sql
│   ├── exportarpdf.py
│   ├── import_excel.py
│   ├── import_usda.py
│   ├── objetivos.py
│   ├── perfiles.py
│   ├── respaldo_restauracion.py
│   └── visualizaciones.py
│
├── docs_contenido.md       # Documentación técnica
├── guia_usuario.md         # Guía paso a paso
├── guia_usuario_nutriapp.pdf
├── reorganizar_estructura.py
├── README.md
└── .gitignore

# 🧪 CLI interactiva de NutriApp

Este es el sistema de menú por terminal de NutriApp. Permite importar alimentos, registrar comidas, obtener resúmenes y mucho más, todo sin abrir la interfaz web.

## 🎯 Funcionalidades disponibles

```python
from scripts.nutri_db import insertar_alimento, insertar_micronutriente, calcular_valores
from scripts.import_usda import importar_desde_usda
from scripts.import_excel import importar_desde_excel
from scripts.comidas import registrar_comida_interactiva
from scripts.consultas import (
    resumen_nutricional_por_comida,
    resumen_diario,
    micronutrientes_dia,
    micronutrientes_semana,
    alimentos_ricos_en_micronutriente,
    crear_comida_ajustada
)

def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL NUTRIAPP")
        print("[1] Registrar alimento manualmente")
        print("[2] Importar alimentos desde USDA")
        print("[3] Importar alimentos desde Excel")
        print("[4] Registrar comida con múltiples alimentos")
        print("[5] Ver resumen nutricional por comida")
        print("[6] Ver resumen nutricional diario")
        print("[7] Consultar nutrientes consumidos por semana")
        print("[8] Buscar alimentos según macros/micros (pendiente)")
        print("[9] Crear comida ajustada a objetivos (pendiente)")
        print("[10] Ver micronutrientes consumidos por día")
        print("[11] Ver micronutrientes consumidos esta semana")
        print("[12] Ver alimentos ricos en un micronutriente")
        print("[13] Sugerir alimentos según objetivos nutricionales")
        print("[14] Ver progreso nutricional semanal en gráfico")
        print("[15] Definir objetivos nutricionales diarios")
        print("[16] Comparar consumo con objetivos en una fecha")
        print("[17] Ver alertas nutricionales (excesos diarios)")
        print("[0] Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            print("(función manual no necesaria si usas USDA/Excel)")
        elif opcion == "2":
            importar_desde_usda()
        elif opcion == "3":
            importar_desde_excel()
        elif opcion == "4":
            registrar_comida_interactiva()
        elif opcion == "5":
            nombre = input("Nombre de la comida: ")
            resumen_nutricional_por_comida(nombre)
        elif opcion == "6":
            fecha = input("Fecha (YYYY-MM-DD): ")
            resumen_diario(fecha)
        elif opcion == "7":
            print("(pendiente)")
        elif opcion == "8":
            print("(pendiente)")
        elif opcion == "9":
            print("(pendiente)")
        elif opcion == "10":
            micronutrientes_dia()
        elif opcion == "11":
            micronutrientes_semana()
        elif opcion == "12":
            alimentos_ricos_en_micronutriente()
        elif opcion == "13":
            crear_comida_ajustada()
        elif opcion == "14":
            graficar_progreso_nutricional()
        elif opcion == "15":
            definir_objetivos()
        elif opcion == "16":
            comparar_objetivos()
        elif opcion == "17":
            fecha = input("📅 Fecha (YYYY-MM-DD): ")
            alertas_diarias(fecha)
        elif opcion == "0":
            print("👋 Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
🚀 Cómo ejecutar el proyecto (modo local)
Clona el repositorio:
git clone https://github.com/Alexmurfitt/ALIMENTACION.git
cd ALIMENTACION

Crea y activa un entorno virtual:
python3.13 -m venv venv
source venv/bin/activate

Instala dependencias:
pip install -r data/requirements.txt

Crea la base de datos en MySQL:
mysql -u tu_usuario -p < scripts/ALIMENTACION.sql

Lanza la app Flask:
cd app
python app.py

Accede desde tu navegador:
http://127.0.0.1:5000

✍️ Autor
Alexander Murfitt Santana
🔗 GitHub: @Alexmurfitt

📜 Licencia
Este proyecto está bajo la licencia MIT.
¡Siéntete libre de usarlo, adaptarlo y compartirlo!

📌 Próximas mejoras (roadmap)
 Filtros por nombre y fecha

 Edición y eliminación de alimentos y comidas

 Login con Flask-Login

 Exportación completa a Excel

 Visualizaciones interactivas con Chart.js

 Estilizado con Bootstrap

 Despliegue online (Render, Fly.io)

 Uso de .env para variables sensibles

 Pruebas automatizadas con pytest

