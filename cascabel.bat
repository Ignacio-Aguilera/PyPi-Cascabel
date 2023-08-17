@ECHO OFF
SET ruta_ejecutable=%~dp0
echo "EJECUTANDO DESDE CASCABEL.BAT (DEVELOP)"
echo %ruta_ejecutable%
echo "======================================="
timeout 3
@ECHO ON
python %ruta_ejecutable%/cascabel.py %1 %2 %3 %4