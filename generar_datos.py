import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Función para generar datos de ventas
def generar_datos_ventas():
    fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
    datos_ventas = {
        'Fecha': [],
        'Producto': [],
        'Monto': []
    }
    
    for fecha in fechas:
        for _ in range(random.randint(1, 5)):  # Número aleatorio de ventas por día
            datos_ventas['Fecha'].append(fecha)
            datos_ventas['Producto'].append(random.choice(productos))
            datos_ventas['Monto'].append(round(random.uniform(10, 100), 2))
    
    df_ventas = pd.DataFrame(datos_ventas)
    df_ventas.to_csv('ventas.csv', index=False)
    print("Datos de ventas generados y guardados en 'ventas.csv'")

# Función para generar datos de vuelos
def generar_datos_vuelos():
    meses = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    años = [2022, 2023]
    datos_vuelos = {
        'Year': [],
        'Month': [],
        'Passengers': []
    }
    
    for año in años:
        for mes in meses:
            datos_vuelos['Year'].append(año)
            datos_vuelos['Month'].append(mes)
            datos_vuelos['Passengers'].append(random.randint(10000, 50000))
    
    df_vuelos = pd.DataFrame(datos_vuelos)
    df_vuelos.to_csv('vuelos.csv', index=False)
    print("Datos de vuelos generados y guardados en 'vuelos.csv'")

# Función para generar datos adicionales si es necesario
def generar_datos_adicionales():
    # Aquí puedes agregar más funciones para generar otros tipos de datos
    pass

# Llamar a las funciones para generar los datos
generar_datos_ventas()
generar_datos_vuelos()
generar_datos_adicionales()
