# Proyecto: Generador de Datos y Análisis Básico

Descripción
----------
Proyecto que genera datos de ejemplo (tiendas, productos, ventas, empleados) y crea análisis gráficos básicos usando pandas y matplotlib. Está pensado para prácticas de analítica y visualización.

Estructura principal
-------------------
- analitica/
  - generarArchivo.py       # Genera archivos CSV de datos de ejemplo
  - analitica.py            # Carga los CSV, genera gráficos y realiza merges
  - datos/                  # Carpeta donde se guardan los CSV generados
  - imagenes/               # Carpeta donde se guardan las imágenes generadas

Requisitos
----------
- Python 3.8+
- Paquetes Python:
  - pandas
  - matplotlib

Instalación
-----------
Instalar dependencias:
```powershell
pip install pandas matplotlib
```

Ejecución
---------
1. Generar los CSV de ejemplo:
```powershell
python analitica\generarArchivo.py
```
Esto crea: `analitica/datos/empleados.csv`, `ventas.csv`, `productos.csv`, `tiendas.csv`.

3. Ejecutar el análisis y generar los gráficos:
```powershell
python analitica\analitica.py
```
Las imágenes se guardan en `analitica/imagenes/`.

Salida
------
- CSVs: analitica/datos/*.csv
- Imágenes: analitica/imagenes/*.png
- Mensajes de consola con información de columnas y confirmación de generación.

Autor
-----------------

Daniela Castro Gómez
