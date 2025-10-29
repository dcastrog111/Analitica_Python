import random
from datetime import datetime, timedelta   
import csv 

# Función para generar fechas aleatorias en 2025
def generar_fecha_aleatoria():
    inicio = datetime(2025, 1, 1)
    fin = datetime(2025, 12, 31)
    return inicio + timedelta(days=random.randint(0, (fin - inicio).days))

# Datos base
tiendas = [
    {"codigo": 1, "nombre": "Tienda A", "ciudad": "Medellín", "direccion": "Calle 1", "gerente": "Juan Pérez", "empleados": 10},
    {"codigo": 2, "nombre": "Tienda B", "ciudad": "Medellín", "direccion": "Calle 2", "gerente": "Ana Gómez", "empleados": 10},
    {"codigo": 3, "nombre": "Tienda C", "ciudad": "Medellín", "direccion": "Calle 3", "gerente": "Luis Rodríguez", "empleados": 10},
    {"codigo": 4, "nombre": "Tienda D", "ciudad": "Medellín", "direccion": "Calle 4", "gerente": "María López", "empleados": 10},
    {"codigo": 5, "nombre": "Tienda E", "ciudad": "Medellín", "direccion": "Calle 5", "gerente": "Carlos Martínez", "empleados": 10},
    {"codigo": 6, "nombre": "Tienda F", "ciudad": "Medellín", "direccion": "Calle 6", "gerente": "Laura Sánchez", "empleados": 10},
    {"codigo": 7, "nombre": "Tienda G", "ciudad": "Medellín", "direccion": "Calle 7", "gerente": "Jorge Torres", "empleados": 10},
    {"codigo": 8, "nombre": "Tienda H", "ciudad": "Medellín", "direccion": "Calle 8", "gerente": "Patricia Ramírez", "empleados": 10},
    {"codigo": 9, "nombre": "Tienda I", "ciudad": "Medellín", "direccion": "Calle 9", "gerente": "Diego Jiménez", "empleados": 10},
    {"codigo": 10, "nombre": "Tienda J", "ciudad": "Medellín", "direccion": "Calle 10", "gerente": "Sofía Castro", "empleados": 10}
]
# Datos de productos 
# Generar al menos 500 productos
productos = []
categorias = ['Camisas', 'Pantalones', 'Zapatos', 'Accesorios', 'Ropa Deportiva']
marcas = ['MarcaA', 'MarcaB', 'MarcaC', 'MarcaD', 'MarcaE']     
for i in range(1, 501):
    producto = {
        "codigo_producto": f"P{i:03}",
        "nombre_producto": f"Producto {i}",
        "categoria": random.choice(categorias),
        "marca": random.choice(marcas),
        "precio_unitario": round(random.uniform(20.0, 200.0), 2),
        "stock_disponible": random.randint(10, 100)
    }
    productos.append(producto)

# Generar datos de ventas
ventas = []     
for _ in range(3000):  # Generar 3000 registros de ventas
    tienda = random.choice(tiendas)
    producto = random.choice(productos)
    cantidad = random.randint(1, 5)
    valor_unitario = producto["precio_unitario"]
    total = round(cantidad * valor_unitario, 2)
    descuento = round(total * random.choice([0, 0.05, 0.10, 0.15]), 2)  # Descuento aleatorio
    venta = {
        "fecha": generar_fecha_aleatoria().strftime("%Y-%m-%d"),
        "codigo_tienda": tienda["codigo"],
        "nombre_tienda": tienda["nombre"],
        "vendedor": f"Vendedor {random.randint(1, tienda['empleados'])}",
        "codigo_producto": producto["codigo_producto"],
        "nombre_producto": producto["nombre_producto"],
        "cantidad": cantidad,
        "valor_unitario": valor_unitario,
        "total": total,
        "descuento": descuento
    }
    ventas.append(venta)

#   Generar datos de empleados
empleados = []
ciudades = ['Medellín', 'Sabaneta', 'Envigado', 'Estrella', 'Bello', 'Itagüí']
generos = ['Masculino', 'Femenino', 'No Binario']
areas = ['Administrativa', 'Servicios Generales', 'Operativos']
niveles_educativos = ['Primaria', 'Secundaria', 'Técnico', 'Tecnólogo', 'Profesional', 'Posgrado']
estados_civiles = ['Soltero', 'Casado', 'Unión Libre', 'Divorciado', 'Viudo']
turnos = ['Diurno', 'Nocturno', 'Mixto']        
for i in range(7000):
    area = random.choices(areas, weights=[0.07, 0.20, 0.73])[0]
    if area == 'Administrativa':
        salario = round(random.uniform(6000000, 8000000), 2)
    elif area == 'Servicios Generales':
        salario = round(random.uniform(2000000, 4000000), 2)
    else:
        salario = round(random.uniform(2000000, 6000000), 2)
    empleado = {
        "ciudad": random.choice(ciudades),
        "genero": random.choices(generos, weights=[0.35, 0.45, 0.20])[0],
        "area": area,
        "salario": salario,
        "edad": random.randint(18, 62),
        "antiguedad": random.randint(0, 40),
        "nivel_educativo": random.choices(niveles_educativos, weights=[0.05,0.25,0.25,0.15,0.25,0.05])[0],
        "estado_civil": random.choice(estados_civiles),
        "hijos": random.choices([0,1,2,3,4], weights=[0.45,0.25,0.15,0.10,0.05])[0],
        "turno": random.choice(turnos),
        "satisfaccion_laboral": round(random.uniform(1, 10), 1)
    }
    empleados.append(empleado)

# Guardar archivo de empleados
with open('analitica/datos/empleados.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=empleados[0].keys())
    writer.writeheader()
    writer.writerows(empleados)


# Guardar archivos CSV
with open('analitica/datos/ventas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=ventas[0].keys())
    writer.writeheader()
    writer.writerows(ventas)
with open('analitica/datos/productos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=productos[0].keys())
    writer.writeheader()
    writer.writerows(productos)
with open('analitica/datos/tiendas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=tiendas[0].keys())
    writer.writeheader()
    writer.writerows(tiendas)   
print("Archivos CSV generados: ventas.csv, productos.csv, tiendas.csv, empleados.csv")
