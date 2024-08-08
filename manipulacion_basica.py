# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:57:30 2024

@author: luis.bravo
"""

import pandas as pd

# Cargar el archvio CSV de ventas
df_ventas = pd.read_csv('ventas.csv')

# Mostrar las primeras filas del DataFrame

print(df_ventas.head())

#INSPECCIÓN DE DATOS

#Inspeccionar el DataFrame
print("Información del DataFrame de ventas:")
print(df_ventas.info())

print("\nDescripción estadística del DataFrame de ventas")
print(df_ventas.describe())

#SELECCIÓN Y FILTRADO DE DATOS:

#Seleccionar una columna
print("\nCoumna 'Monto':")
print(df_ventas['Monto'])

#Seleccionar múltiples columnas
print("\nColumnas 'Fecha' y 'Monto':")
print(df_ventas[['Fecha', 'Monto']])

#Filtrar filas donde el valor de 'Monto' es mayour que 50
print("\nFilas donde 'Monto' > 50:")
print(df_ventas[df_ventas['Monto'] > 50])


#LIMPIEZA DE DATOS
#Crear un DataFrame con valores nulos

data = {'A':[1,2,None,4],
        'B':[None, 2,3,4]}
df_null = pd.DataFrame(data)

print("\nDataFrame con valores nulos:")
print(df_null)


#Manejar valores nulos
df_null_filled = df_null.fillna(0)
print("\nDataFrame con valores nulos llenados con 0:")
print(df_null_filled)

#Convertir tipos de datos
df_ventas['Monto'] = df_ventas['Monto'].astype(float)

print("\nTipo de datos de la columna 'Monto' despúes de la convesión:")
print(df_ventas.dtypes)
















