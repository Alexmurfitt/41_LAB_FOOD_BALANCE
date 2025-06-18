# 🔄 Flujo de Datos - NutriApp

Este documento describe cómo fluye la información dentro de NutriApp desde la fuente de datos hasta la generación de informes y visualizaciones.

---

## 🛠️ Fuentes de datos iniciales

- **USDA CSV** (`FoodData_Central`) → importación masiva vía script `import_usda.py`
- **Excel personal** (`DIETA COMPLETA.xlsx`) → importación manual o semiautomática con `import_excel.py`

---

## 🧩 Transformación y registro

- Los datos de alimentos son parseados y almacenados en la tabla `alimentos`
- Los micronutrientes asociados a cada alimento van a la tabla `micronutrientes`

```
Excel/CSV → import_usda.py / import_excel.py
            ↓
          alimentos + micronutrientes (tablas)
```

---

## 🍽️ Registro de comidas

El usuario puede registrar comidas desde CLI con múltiples alimentos y cantidades:

- Se crea una entrada en la tabla `comidas`
- Por cada alimento registrado, se genera una fila en `comida_alimentos` con cálculos automáticos:
  - kcal = (g / 100) * kcal_alimento
  - idem para macros

```
CLI / UI Web → registrar_comida_interactiva()
                ↓
        comidas + comida_alimentos
```

---

## 📈 Visualización / Reportes

Una vez registrados los alimentos y comidas:

- El usuario puede consultar macros y micros por día, semana, comida
- Reportes PDF diarios y semanales disponibles
- Exportación de base completa a Excel
- Visualización con gráficos (semana, objetivos)

```
comidas + comida_alimentos
       ↓
  consultas.py / visualizaciones.py / exportar_pdf.py
       ↓
   Informes → PDF / Gráficos / Excel
```

---

## 🛡️ Respaldos / Exportaciones

- Toda la base puede respaldarse (`respaldos/`) y restaurarse automáticamente
- Se puede exportar en cualquier momento a:
  - `base_nutricional_exportada.xlsx`
  - `informe_nutricional_YYYY-MM-DD.pdf`

---

## 🧭 Esquema General

```
Importar datos  →  Guardar en MySQL  →  Registrar comidas  →  Consultas + Reportes  →  Exportar/Respaldar
     ↑                                                   ↓                      ↓
   USDA / Excel                             CLI / UI Web          PDF / Excel / Visual
```

> Este flujo modular permite flexibilidad, escalabilidad y automatización total del sistema.
