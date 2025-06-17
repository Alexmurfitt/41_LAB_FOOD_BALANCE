# cli.py

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
from scripts.visualizaciones import graficar_progreso_nutricional
from scripts.objetivos import definir_objetivos, comparar_objetivos

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
