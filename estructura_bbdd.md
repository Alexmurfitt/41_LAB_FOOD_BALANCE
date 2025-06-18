
### `estructura_bbdd.md`

```markdown
# 📐 Estructura de la Base de Datos

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
