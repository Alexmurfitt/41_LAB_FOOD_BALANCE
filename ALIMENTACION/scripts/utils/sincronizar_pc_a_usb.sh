#!/bin/bash

PC_PATH="/home/reboot-student/code/ALIMENTACION"
USB_PATH="/media/reboot-student/ESD-USB/ALIMENTACION"

echo "🔄 Sincronizando archivos del PC al USB..."
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
    "scripts/core/objetivos.py"
    "scripts/core/perfiles.py"
    "scripts/core/alertas.py"
    "scripts/core/ASIG_ALIM.py"
    "scripts/core/ASIG_ALIM_CANT.py"
)

for item in "${REQUIRED_ITEMS[@]}"; do
    PC_ITEM="$PC_PATH/$item"
    USB_ITEM="$USB_PATH/$item"

    if [ -f "$PC_ITEM" ]; then
        echo "🟢 Copiando '$item' al USB..."
        sudo mkdir -p "$(dirname "$USB_ITEM")"
        sudo cp "$PC_ITEM" "$USB_ITEM"
    else
        echo "❌ '$item' no encontrado en el PC"
    fi
done

echo -e "\n✅ Sincronización completada."

