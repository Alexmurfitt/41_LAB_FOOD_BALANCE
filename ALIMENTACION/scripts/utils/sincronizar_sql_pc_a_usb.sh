#!/bin/bash

PC_SQL="$HOME/code/ALIMENTACION/scripts/sql/ALIMENTACION.sql"
USB_SQL="/media/reboot-student/ESD-USB/ALIMENTACION/scripts/sql/ALIMENTACION.sql"

echo "🔄 Sincronizando archivo SQL del PC al USB..."

# Verificar que el archivo existe en el PC
if [ ! -f "$PC_SQL" ]; then
    echo "❌ El archivo $PC_SQL no existe."
    exit 1
fi

# Crear carpeta destino en USB si no existe
mkdir -p "$(dirname "$USB_SQL")"

# Copiar archivo
sudo cp "$PC_SQL" "$USB_SQL"

echo "✅ Archivo SQL actualizado en el USB correctamente."
