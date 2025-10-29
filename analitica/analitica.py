
import pandas as pd
import matplotlib.pyplot as plt     
from pathlib import Path

#crear analítica para realizar procesos de gráficos con matplotlib


#crear analitica para empleados.csv
base_dir = Path(__file__).parent / 'datos'
base_dir2 = Path(__file__).parent / 'imagenes'
empleados_df = pd.read_csv(base_dir / 'empleados.csv')      
productos_df = pd.read_csv(base_dir / 'productos.csv')
tiendas_df = pd.read_csv(base_dir / 'tiendas.csv')
ventas_df = pd.read_csv(base_dir / 'ventas.csv')
print("Archivos cargados correctamente.")


# Normalizar nombres de columnas (sin espacios y en minúsculas)
empleados_df.columns = empleados_df.columns.str.strip().str.lower()
productos_df.columns = productos_df.columns.str.strip().str.lower()
tiendas_df.columns = tiendas_df.columns.str.strip().str.lower()
ventas_df.columns = ventas_df.columns.str.strip().str.lower()   
print("Columnas empleados:", empleados_df.columns.tolist())
print("Columnas productos:", productos_df.columns.tolist()) 
print("Columnas tiendas:", tiendas_df.columns.tolist())
print("Columnas ventas:", ventas_df.columns.tolist())
ventas_df['fecha'] = pd.to_datetime(ventas_df['fecha'], errors='coerce')


#crear analitica para empleados.csv
#1 agrupar los datos por genero y contar el numero de empleados de cada grupo
empleados_genero = empleados_df.groupby('genero').size()
print("Número de empleados por género:")
print(empleados_genero)

#2 grafico circular de la distribución de genero colocar etiquetas y porcentaje titulo distribucion
#de genero y guardar la imagen como genero_pastel.png

#2 grafico circular (2D) de la distribución de genero con etiquetas y porcentaje, guardar como genero_pastel.png
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)  # eje 2D: pie no funciona en Axes3D
ax.pie(empleados_genero, labels=empleados_genero.index, autopct='%1.1f%%', startangle=140, shadow=True)
ax.set_title('Distribución de género')
out_path = base_dir2 / 'genero_pastel.png'
plt.savefig(out_path)
# plt.show()

#crear analitica para empleados.csv
#1 grafico de barras por ciudad con etiquetas y titulo empleados por ciudad
empleados_ciudad = empleados_df['ciudad'].value_counts()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(empleados_ciudad.index, empleados_ciudad.values)
ax.set_xlabel('Ciudad')
ax.set_ylabel('Número de empleados')
ax.set_title('Empleados por ciudad')
plt.xticks(rotation=45)
out_path = base_dir2 / 'empleados_por_ciudad.png'
plt.savefig(out_path)
# plt.show()

#crear analitica para productos.csv
#1 grafico de barras horizontales por categoria con etiquetas y titulo productos por categoria  
productos_categoria = productos_df['categoria'].value_counts()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.barh(productos_categoria.index, productos_categoria.values)
ax.set_xlabel('Número de productos')
ax.set_ylabel('Categoría')
ax.set_title('Productos por categoría')
plt.xticks(rotation=45)
out_path = base_dir2 / 'productos_por_categoria.png'
plt.savefig(out_path)
# plt.show()  

#2 grafico de barras por marca con etiquetas y titulo productos por marca  
productos_marca = productos_df['marca'].value_counts()  
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.barh(productos_marca.index, productos_marca.values)
ax.set_xlabel('Número de productos')
ax.set_ylabel('Marca')
ax.set_title('Productos por marca')
plt.xticks(rotation=45)
out_path = base_dir2 / 'productos_por_marca.png'
plt.savefig(out_path)
# plt.show()

#crear analitica para tiendas.csv
#1 grafico de barras por ciudad con etiquetas y titulo tiendas por ciudad
tiendas_ciudad = tiendas_df['ciudad'].value_counts()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(tiendas_ciudad.index, tiendas_ciudad.values)
ax.set_xlabel('Ciudad')
ax.set_ylabel('Número de tiendas')
ax.set_title('Tiendas por ciudad')
plt.xticks(rotation=45)
out_path = base_dir2 / 'tiendas_por_ciudad.png'
plt.savefig(out_path)
# plt.show()

#crear analitica para ventas.csv
#1 grafico de barras por producto con etiquetas y titulo ventas por producto
ventas_producto = ventas_df['nombre_producto'].value_counts()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(ventas_producto.index, ventas_producto.values)
ax.set_xlabel('Producto')   
ax.set_ylabel('Número de ventas')
ax.set_title('Ventas por producto')
plt.xticks(rotation=45)
out_path = base_dir2 / 'ventas_por_producto.png'
plt.savefig(out_path)
# plt.show()
#2 grafico de barras por tienda con etiquetas y titulo ventas por tienda
ventas_tienda = ventas_df['nombre_tienda'].value_counts()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)   
ax.bar(ventas_tienda.index, ventas_tienda.values)
ax.set_xlabel('Tienda')
ax.set_ylabel('Número de ventas')
ax.set_title('Ventas por tienda')
plt.xticks(rotation=45)
out_path = base_dir2 / 'ventas_por_tienda.png'
plt.savefig(out_path)
# plt.show()
#3 grafico de barras por fecha-mes con etiquetas y titulo ventas por fecha
ventas_fecha = ventas_df['fecha'].dt.to_period('M').value_counts().sort_index()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.bar(ventas_fecha.index.astype(str), ventas_fecha.values)
ax.set_xlabel('Fecha (Mes)')
ax.set_ylabel('Número de ventas')
ax.set_title('Ventas por fecha')
plt.xticks(rotation=45)
out_path = base_dir2 / 'ventas_por_fecha.png'
plt.savefig(out_path)
# plt.show()
print("Análisis y gráficos generados correctamente.")

#realizo relacionamiento entre los archivos empleadoscsv, productos.csv , tiendas.csv y ventas.csv
#empleados con tiendas por ciudad
empleados_tiendas = pd.merge(empleados_df, tiendas_df, left_on='ciudad', right_on='ciudad', suffixes=('_empleado', '_tienda'))
print("Relación empleados con tiendas por ciudad:")
print(empleados_tiendas)
#ventas con productos por producto
ventas_productos = pd.merge(ventas_df, productos_df, left_on='nombre_producto', right_on='nombre_producto', suffixes=('_venta', '_producto'))
print("Relación ventas con productos por producto:")    
print(ventas_productos)     
#ventas con tiendas por tienda
ventas_tiendas = pd.merge(ventas_df, tiendas_df, left_on='nombre_tienda', right_on='nombre', suffixes=('_venta', '_tienda'))
print("Relación ventas con tiendas por tienda:")
print(ventas_tiendas)
print("Relaciones entre archivos generadas correctamente.")
