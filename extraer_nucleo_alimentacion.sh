#!/bin/bash

# Ruta origen (ajusta si es necesario)
ORIGEN="$HOME/code/ALIMENTACION"
DESTINO="$HOME/code/FOOD_BALANCE_CORE"

# Crear directorio destino si no existe
mkdir -p "$DESTINO"

echo "📦 Copiando núcleo esencial desde: $ORIGEN"
echo "➡️  Destino: $DESTINO"
echo

# Copiar scripts esenciales de app
mkdir -p "$DESTINO/app/templates"
cp "$ORIGEN/app/app.py" "$DESTINO/app/"
cp "$ORIGEN/app/cli.py" "$DESTINO/app/"
cp "$ORIGEN/app/templates/"*.html "$DESTINO/app/templates/" 2>/dev/null || true

# Copiar scripts útiles
cp "$ORIGEN"/scripts/*.py "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/scripts/utils/*.py "$DESTINO/" 2>/dev/null || true

# Copiar configuración y dependencias
cp "$ORIGEN"/data/nutri_db.py "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/data/requirements.txt "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/config.py "$DESTINO/" 2>/dev/null || true

# Copiar SQL útil (estructura y datos)
mkdir -p "$DESTINO/sql"
cp "$ORIGEN"/data/esquema.sql "$DESTINO/sql/" 2>/dev/null || true
cp "$ORIGEN"/data/comidas.sql "$DESTINO/sql/" 2>/dev/null || true

# Copiar documentación clave
cp "$ORIGEN"/README.md "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/docs_contenido.md "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/docs/*.md "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/docs/*.pdf "$DESTINO/" 2>/dev/null || true

# Copiar archivos auxiliares útiles
cp "$ORIGEN"/reorganizar_estructura.py "$DESTINO/" 2>/dev/null || true
cp "$ORIGEN"/propuesta_chatgpt.txt "$DESTINO/" 2>/dev/null || true

echo "✅ Extracción completada."
echo "🔎 Puedes revisar el directorio $DESTINO"

