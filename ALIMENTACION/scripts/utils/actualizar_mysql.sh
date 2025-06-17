#!/bin/bash

# Variables
DB="ALIMENTACION"
USER="root"
PASS="0000"
SQL_FILE="scripts/sql/ALIMENTACION.sql"

echo "🚀 Iniciando actualización de la base de datos '$DB'..."

# 1. Borrar datos antiguos
echo "🧹 Limpiando tablas existentes..."
mysql -u $USER -p$PASS $DB <<EOF_SQL
DELETE FROM meal_items;
DELETE FROM meals;
DELETE FROM foods;
EOF_SQL

# 2. Importar datos actualizados desde el SQL
echo "📦 Importando datos desde $SQL_FILE..."
mysql -u $USER -p$PASS $DB < $SQL_FILE

echo "✅ Actualización completada correctamente."
