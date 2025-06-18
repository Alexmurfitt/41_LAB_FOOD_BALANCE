# 📘 Guía de Usuario - NutriApp

**NutriApp** es una aplicación para gestionar, analizar y optimizar tu alimentación diaria mediante el registro preciso de alimentos, comidas, macronutrientes y micronutrientes.

---

## 🧱 Estructura del Proyecto

```
ALIMENTACION/
├── data/                       # Excel de dieta y datos USDA
├── nutriapp/                   # Aplicación Flask (interfaz web)
├── scripts/                    # Módulos funcionales en Python
├── README.md                   # Documentación general
└── cli.py                      # Interfaz de línea de comandos
```

---

## 🧭 Cómo empezar

```bash
# Clona el proyecto
$ git clone git@github.com:Alexmurfitt/ALIMENTACION.git
$ cd ALIMENTACION

# Crea y activa entorno virtual
$ python3.13 -m venv venv
$ source venv/bin/activate

# Instala dependencias
$ pip install -r requirements.txt
```

---

## 🖥️ Menú CLI (`cli.py`)

Ejecuta:
```bash
python cli.py
```
Y accede a funcionalidades como:

- [2] Importar datos desde USDA
- [3] Importar alimentos desde Excel
- [4] Registrar comidas
- [5-6] Ver resúmenes por comida y día
- [10-11] Consultar micronutrientes
- [14] Ver gráfico semanal
- [22] Ver macros por tipo de comida (etiqueta)
- [23-24] Exportar informes diarios/semanales en PDF
- [25] Exportar toda la base de datos a Excel
- [26-27] Respaldar o restaurar todo el sistema

---

## 🧪 Ejemplo de Registro de Comida

```
🍽️ Registrar nueva comida
Nombre de la comida: Comida 1
Fecha (YYYY-MM-DD): 2025-04-05
Etiqueta: post-entreno
Nombre del alimento: Avena
Cantidad en gramos: 60
✅ Alimento añadido a la comida.
```

---

## 📄 Exportar Informes

- `informe_nutricional_YYYY-MM-DD.pdf`
- `informe_semanal_YYYYMMDD_YYYYMMDD.pdf`
- `base_nutricional_exportada.xlsx`

---

## 🔐 Sistema de Respaldo

```bash
[26] Crear respaldo completo del sistema
[27] Restaurar desde un respaldo anterior
```
Los archivos se almacenan en la carpeta `respaldos/` y permiten volver a un estado anterior.

---

## ✍️ Autor
**Alexander Murfitt Santana**

---

## 🔗 Licencia
MIT – Uso libre para propósitos personales, educativos y profesionales.
