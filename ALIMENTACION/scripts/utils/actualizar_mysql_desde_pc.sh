#!/bin/bash

PC_SQL="$HOME/code/ALIMENTACION/scripts/sql/ALIMENTACION.sql"
USB_SQL_DIR="/media/reboot-student/ESD-USB/ALIMENTACION/scripts/sql"
USB_SQL="$USB_SQL_DIR/ALIMENTACION.sql"

echo "🔄 Sincronizando archivo SQL del PC al USB..."

# Verificar que el archivo existe en el PC
if [ ! -f "$PC_SQL" ]; then
    echo "❌ El archivo $PC_SQL no existe."
    exit 1
fi

# Verificar si hay un archivo conflictivo en vez de una carpeta
if [ -f "$USB_SQL_DIR" ]; then
    echo "⚠️  Atención: '$USB_SQL_DIR' es un archivo, no una carpeta. Eliminando..."
    sudo rm -f "$USB_SQL_DIR"
fi

# Crear carpeta si no existe
sudo mkdir -p "$USB_SQL_DIR"

# Copiar archivo SQL
sudo cp "$PC_SQL" "$USB_SQL"

echo "✅ Archivo SQL actualizado en el USB correctamente."

echo ""
echo "💾 Actualizando base de datos MySQL desde $PC_SQL..."
mysql -u root -p0000 < "$PC_SQL"

if [ $? -eq 0 ]; then
    echo "✅ Base de datos MySQL actualizada correctamente desde $PC_SQL."
else
    echo "❌ Error al importar el archivo SQL."
fi

