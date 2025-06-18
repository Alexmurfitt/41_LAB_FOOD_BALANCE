#!/bin/bash

# Ruta origen
ORIGEN="$HOME/code/ALIMENTACION"
DESTINO="$HOME/code/labs/41_LAB_FOOD_BALANCE"

echo "📦 Moviendo archivos desde: $ORIGEN"
echo "➡️  Hacia: $DESTINO"
echo

# Crear carpetas necesarias
mkdir -p "$DESTINO/app/templates"
mkdir -p "$DESTINO/sql"

# Mover scripts de app
mv -u "$ORIGEN/app/app.py" "$DESTINO/app/" 2>/dev/null || true
mv -u "$ORIGEN/app/cli.py" "$DESTINO/app/" 2>/dev/null || true
mv -u "$ORIGEN/app/templates/"*.html "$DESTINO/app/templates/" 2>/dev/null || true

# Mover scripts sueltos
mv -u "$ORIGEN"/scripts/*.py "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/scripts/utils/*.py "$DESTINO/" 2>/dev/null || true

# Configuración
mv -u "$ORIGEN"/data/nutri_db.py "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/data/requirements.txt "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/config.py "$DESTINO/" 2>/dev/null || true

# SQL
mv -u "$ORIGEN"/data/esquema.sql "$DESTINO/sql/" 2>/dev/null || true
mv -u "$ORIGEN"/data/comidas.sql "$DESTINO/sql/" 2>/dev/null || true

# Documentación clave
mv -u "$ORIGEN"/README.md "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/docs_contenido.md "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/docs/*.md "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/docs/*.pdf "$DESTINO/" 2>/dev/null || true

# Archivos auxiliares
mv -u "$ORIGEN"/reorganizar_estructura.py "$DESTINO/" 2>/dev/null || true
mv -u "$ORIGEN"/propuesta_chatgpt.txt "$DESTINO/" 2>/dev/null || true

echo "✅ Movimiento completado."
echo "🔎 Archivos trasladados a $DESTINO"
