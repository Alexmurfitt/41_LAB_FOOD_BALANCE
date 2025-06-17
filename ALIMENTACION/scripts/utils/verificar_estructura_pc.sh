#!/bin/bash

PC_PATH="$HOME/code/ALIMENTACION"

echo "📁 Verificando estructura del proyecto en el PC: $PC_PATH"
echo "-------------------------------------------"

REQUIRED_DIRS=(
    "app" "app/templates" "config" "data" "data/Fooddata_usda"
    "docs" "scripts" "scripts/core" "scripts/utils"
    "scripts/ingestion" "scripts/sql"
)

REQUIRED_FILES=(
    "README.md" "LICENSE" "reorganizar_estructura.py" "propuesta_chatgpt.txt"
    "docs/guia_usuario.md" "docs/guia_usuario_nutriapp.pdf"
    "data/DIETA COMPLETA.xlsx" "data/esquema.sql" "data/comidas.sql"
    "data/nutri_db.py" "data/requirements.txt"
    "scripts/core/comidas.py" "scripts/utils/exportarpdf.py"
    "scripts/ingestion/import_excel.py" "scripts/sql/ALIMENTACION.sql"
)

echo "📂 Verificando carpetas..."
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$PC_PATH/$dir" ]; then
        echo "✔️  $dir"
    else
        echo "❌  Falta carpeta: $dir"
    fi
done

echo -e "\n📄 Verificando archivos..."
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$PC_PATH/$file" ]; then
        echo "✔️  $file"
    else
        echo "❌  Falta archivo: $file"
    fi
done

echo -e "\n✅ Verificación finalizada."
