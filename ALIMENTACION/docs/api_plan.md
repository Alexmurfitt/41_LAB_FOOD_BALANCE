# 🌐 API Plan - NutriApp REST

Diseño de una futura API RESTful para NutriApp, que permita consultar y manipular datos nutricionales desde apps externas, móvil o interfaces web avanzadas.

---

## 📦 Recursos (Endpoints principales)

### 🔍 Alimentos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/alimentos         | Lista todos los alimentos registrados |
| GET    | /api/alimentos/<id>    | Detalles de un alimento específico |
| POST   | /api/alimentos         | Añadir un nuevo alimento |
| PUT    | /api/alimentos/<id>    | Editar alimento existente |
| DELETE | /api/alimentos/<id>    | Eliminar un alimento |

### 🧪 Micronutrientes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/alimentos/<id>/micros | Listar micronutrientes de un alimento |
| POST   | /api/micronutrientes        | Añadir nuevo micronutriente |

### 🍽️ Comidas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/comidas         | Listar comidas |
| POST   | /api/comidas         | Crear nueva comida |
| GET    | /api/comidas/<id>    | Ver composición de una comida |
| DELETE | /api/comidas/<id>    | Eliminar comida |

### 📊 Resúmenes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/resumen/diario/<fecha>  | Resumen de nutrientes en una fecha |
| GET    | /api/resumen/semana/<yyyy-mm-dd> | Resumen semanal desde fecha |
| GET    | /api/resumen/etiqueta        | Resumen por tipo de comida |

### 🎯 Objetivos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/objetivos/<fecha>  | Consultar objetivos del día |
| POST   | /api/objetivos          | Definir o actualizar objetivos |

### 👤 Perfiles
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /api/perfiles              | Listar perfiles guardados |
| POST   | /api/perfiles              | Crear nuevo perfil nutricional |
| PUT    | /api/perfiles/<id>        | Editar un perfil |
| PATCH  | /api/perfil/activo/<id>   | Activar perfil actual |

---

## ⚙️ Framework propuesto

- `FastAPI` (recomendado por su rendimiento, documentación automática y soporte async)

## 🔐 Autenticación futura

- Token JWT opcional si se decide multicuenta
- Límite de acceso por IP (si se hace público)

---

## 🚀 Posibles Usos

- Apps móviles para seguimiento nutricional
- Dashboards personalizados en web
- Integración con sistemas de entrenamiento, ayuno, sueño, etc.

---

> Esta API puede desplegarse en un contenedor Docker con base FastAPI + MySQL y servir como backend profesional escalable.
