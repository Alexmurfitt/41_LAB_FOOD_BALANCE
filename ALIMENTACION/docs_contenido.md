# 📚 Documentación Técnica - NutriApp

Este directorio `docs/` contiene recursos avanzados para desarrolladores y usuarios técnicos que quieran extender o adaptar NutriApp a sus necesidades.

---

## 📁 Archivos incluidos

### `estructura_bbdd.md`
Explica la estructura completa de la base de datos (tablas, relaciones, claves externas).

### `consultas_avanzadas.sql`
Colección de queries útiles para analizar, auditar o extender la funcionalidad.

### `api_plan.md`
Diseño propuesto para una futura API REST para NutriApp (usando Flask-RESTful o FastAPI).

### `flujo_datos.md`
Diagrama de flujo de los datos desde entrada (Excel o USDA) hasta visualización (gráficos, informes).

### `notas_migracion.md`
Guía para migrar la base de datos o el proyecto a otro entorno.

---

## 🧠 Objetivo de esta carpeta
- Tener un lugar claro para mantener el conocimiento del sistema
- Facilitar colaboración futura con otros desarrolladores
- Servir de base para publicar documentación pública si así lo deseas

---

## 📐 estructura_bbdd.md

### Tablas principales:

- `alimentos` → contiene información base de cada alimento (100g):
  - `id` (PK), `nombre`, `kcal`, `proteinas`, `carbohidratos`, `grasas`

- `micronutrientes` → micronutrientes asociados a alimentos:
  - `id`, `alimento_id` (FK), `nombre`, `cantidad_mg`

- `comidas` → comidas registradas por fecha:
  - `id`, `nombre`, `fecha`, `etiqueta`

- `comida_alimentos` → relación N:M entre comidas y alimentos:
  - `id`, `comida_id` (FK), `alimento_id` (FK), `cantidad_g`, `total_kcal`, `total_protein`, `total_carbs`, `total_fat`

- `objetivos` → objetivos nutricionales definidos:
  - `id`, `fecha`, `kcal`, `proteinas`, `carbohidratos`, `grasas`

- `perfiles` → perfiles nutricionales personalizables:
  - `id`, `nombre`, `descripcion`, `kcal`, `proteinas`, `carbohidratos`, `grasas`

- `alertas` → para registrar excesos (pendiente de automatización):
  - `id`, `fecha`, `tipo`, `mensaje`

### Relaciones:
- `micronutrientes.alimento_id → alimentos.id`
- `comida_alimentos.comida_id → comidas.id`
- `comida_alimentos.alimento_id → alimentos.id`

---

> Esta estructura permite: registrar comidas, consultar totales por día o semana, generar informes, definir objetivos y exportar o respaldar todo fácilmente.
