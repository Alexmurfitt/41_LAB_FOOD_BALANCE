#!/bin/bash

USB_PATH="/media/reboot-student/ESD-USB/ALIMENTACION"
PC_PATH="$HOME/code/ALIMENTACION"

echo "🔍 Comparando estructuras entre USB y PC..."
echo "---------------------------------------------"

declare -a REQUIRED_ITEMS=(
    "README.md"
    "LICENSE"
    "reorganizar_estructura.py"
    "propuesta_chatgpt.txt"
    "docs/guia_usuario.md"
    "docs/guia_usuario_nutriapp.pdf"
    "data/DIETA COMPLETA.xlsx"
    "data/esquema.sql"
    "data/comidas.sql"
    "data/nutri_db.py"
    "data/requirements.txt"
    "scripts/core/comidas.py"
    "scripts/utils/exportarpdf.py"
    "scripts/ingestion/import_excel.py"
    "scripts/sql/ALIMENTACION.sql"
)

for item in "${REQUIRED_ITEMS[@]}"; do
    USB_ITEM="$USB_PATH/$item"
    PC_ITEM="$PC_PATH/$item"

    if [ -f "$USB_ITEM" ] && [ ! -f "$PC_ITEM" ]; then
        echo "🟡 Archivo '$item' está en USB pero NO en el PC. Copiando..."
        mkdir -p "$(dirname "$PC_ITEM")"
        cp "$USB_ITEM" "$PC_ITEM"
    elif [ ! -f "$USB_ITEM" ] && [ -f "$PC_ITEM" ]; then
        echo "🟠 Archivo '$item' está en el PC pero NO en el USB."
    elif [ ! -f "$USB_ITEM" ] && [ ! -f "$PC_ITEM" ]; then
        echo "❌ Archivo '$item' no existe en ningún lado."
    else
        echo "✔️  Archivo '$item' ya está en ambos sitios."
    fi
done

echo -e "\n✅ Comparación y sincronización completada."
