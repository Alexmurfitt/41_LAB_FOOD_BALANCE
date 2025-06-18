# ⚙️ Ruta raíz del proyecto (ajusta si es necesario)
$root = "D:\REBOOT ACADEMY\41_LAB_FOOD_BALANCE"
Set-Location $root

# ✅ Crear carpetas destino si no existen
$estructura = @("core", "ui", "data", "utils", "docs", "database", "templates", "assets")
foreach ($folder in $estructura) {
    if (-not (Test-Path "$root\$folder")) {
        New-Item -Path "$root\$folder" -ItemType Directory | Out-Null
    }
}

# 🚀 Mover scripts por tipo
Move-Item "$root\app\app.py" -Destination "$root\ui\" -Force
Move-Item "$root\app\cli.py" -Destination "$root\ui\" -Force
Move-Item "$root\models.py" -Destination "$root\core\" -Force
Move-Item "$root\visualizaciones.py" -Destination "$root\ui\" -Force
Move-Item "$root\exportarpdf.py" -Destination "$root\utils\" -Force
Move-Item "$root\reorganizar_estructura.py" -Destination "$root\utils\" -Force
Move-Item "$root\respaldo_restauracion.py" -Destination "$root\utils\" -Force
Move-Item "$root\init_db.py" -Destination "$root\database\" -Force
Move-Item "$root\nutri_db.py" -Destination "$root\data\" -Force
Move-Item "$root\consultas.py" -Destination "$root\database\" -Force

# 🧾 Mover documentación
Get-ChildItem -Path $root -Include *.md,*.pdf -File | ForEach-Object {
    Move-Item $_.FullName -Destination "$root\docs\" -Force
}

# 🗃️ Mover SQL
Move-Item "$root\sql\*.sql" -Destination "$root\database\" -Force
Remove-Item "$root\sql" -Recurse -Force

# 🌐 Mover HTML
Move-Item "$root\index.html" -Destination "$root\ui\" -Force
Move-Item "$root\app\templates\*" -Destination "$root\templates\" -Force
Remove-Item "$root\app\templates" -Recurse -Force

# 🖼️ Mover assets (imágenes)
Move-Item "$root\hero-bg.png" -Destination "$root\assets\" -Force
Move-Item "$root\video-placeholder.png" -Destination "$root\assets\" -Force

# 🧹 Limpiar carpetas vacías
$vacias = Get-ChildItem -Directory | Where-Object { @(Get-ChildItem $_.FullName -Recurse -Force).Count -eq 0 }
$vacias | ForEach-Object { Remove-Item $_.FullName -Recurse -Force }

# ✅ Confirmación final
Write-Host "✅ Organización completada con éxito."
