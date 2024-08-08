# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:49:18 2024

@author: luis.bravo
"""
import pandas as pd


# Cargar el archivo de CSV de ventas
df_ventas = pd.read_csv('ventas.csv')

# Mostrar las primeras filas del Dataframe
print(df_ventas.head())

# Inspeccionar el DataFrame
print("\nInformación del DataFrame de ventas:")
print(df_ventas.info())

print("\nDescripción estadística del DataFrame de ventas:")
print(df_ventas.describe())

# Limpieza y preparación de datos:

# MAnejar valores nulos si los hay
df_ventas = df_ventas.fillna(0)

# Convertir tipos de datos si es necesario
df_ventas['Monto'] = df_ventas['Monto'].astype(float)

# ANÁLISIS DESCRIPTIVO

# Calcular el total de ventas
total_ventas = df_ventas['Monto'].sum()
print("\nTotal de ventas:", total_ventas)

# Calcular el promedio de ventas
promedio_ventas = df_ventas['Monto'].mean()
print("Promedio de ventas:", promedio_ventas)