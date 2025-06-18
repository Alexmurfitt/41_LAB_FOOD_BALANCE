📋 MENÚ PRINCIPAL NUTRIAPP

[1] Registrar alimento manualmente
[2] Importar alimentos desde USDA
[3] Importar alimentos desde Excel
[4] Registrar comida con múltiples alimentos
[5] Calcular valores por comida/día
[6] Consultar nutrientes consumidos por semana
[7] Buscar alimentos según macros/micros
[8] Crear comida ajustada a objetivos
[9] Ver resumen nutricional de un día
[0] Salir

# cli.py

from scripts.nutri_db import insertar_alimento, insertar_micronutriente, calcular_valores
from scripts.import_usda import importar_desde_usda
from scripts.import_excel import importar_desde_excel
from scripts.consultas import ejecutar_consulta_nutricional
from scripts.resumen import mostrar_resumen_diario


def menu():
    while True:
        print("\n📋 MENÚ PRINCIPAL NUTRIAPP")
        print("[1] Registrar alimento manualmente")
        print("[2] Importar alimentos desde USDA")
        print("[3] Importar alimentos desde Excel")
        print("[4] Registrar comida con múltiples alimentos")
        print("[5] Calcular valores por comida/día")
        print("[6] Consultar nutrientes consumidos por semana")
        print("[7] Buscar alimentos según macros/micros")
        print("[8] Crear comida ajustada a objetivos")
        print("[9] Ver resumen nutricional de un día")
        print("[0] Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre del alimento: ")
            prote = float(input("Proteínas por 100g: "))
            carbs = float(input("Carbohidratos por 100g: "))
            grasas = float(input("Grasas por 100g: "))
            kcal = (prote * 4) + (carbs * 4) + (grasas * 9)
            alimento_id = insertar_alimento(nombre, prote, carbs, grasas, kcal)
            print(f"✅ Alimento '{nombre}' guardado con ID {alimento_id}.")

            agregar_micros = input("¿Agregar micronutrientes? (s/n): ").lower()
            while agregar_micros == "s":
                micro = input("  Nombre del micronutriente: ")
                valor = float(input(f"  Cantidad por 100g (mg): "))
                insertar_micronutriente(alimento_id, micro, valor)
                agregar_micros = input("¿Agregar otro? (s/n): ").lower()

        elif opcion == "2":
            importar_desde_usda()

        elif opcion == "3":
            importar_desde_excel()

        elif opcion == "4":
            print("(función por implementar: registrar comida)")

        elif opcion == "5":
            print("(función por implementar: calcular por comida/día)")

        elif opcion == "6":
            ejecutar_consulta_nutricional("semanal")

        elif opcion == "7":
            ejecutar_consulta_nutricional("alimentos")

        elif opcion == "8":
            ejecutar_consulta_nutricional("objetivos")

        elif opcion == "9":
            mostrar_resumen_diario()

        elif opcion == "0":
            print("👋 Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()

