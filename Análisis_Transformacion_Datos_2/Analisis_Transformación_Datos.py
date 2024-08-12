# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:34:07 2024

@author: luis.bravo
"""

import pandas as pd


# Cargar el archivo CSV

df_ventas = pd.read_csv('ventas_erroneas.csv')

# Convertir 'Monto' a numérico, forzando errores a NaN
df_ventas['Monto'] = pd.to_numeric(df_ventas['Monto'], errors='coerce')

# Agrupar por 'Producto' y sumar los montos
grupo_producto = df_ventas.groupby('Producto')['Monto'].sum()

# Mostrar los resultados
print(grupo_producto)

# Aplicación de funciones: 'apply' y 'map'

# Definiendo una función de limpieza
# Función para limpiar fechas

def limpiar_fecha(fecha):
    try:
        return pd.to_datetime(fecha)
    except:
        return pd.NaT # Not a Time, similar a NaN para fechas

# Aplicar la funicón de limpieza
df_ventas['Fecha'] = df_ventas['Fecha'].apply(limpiar_fecha)

# Mostrar las primeras filas para verificar
print(df_ventas.head())

