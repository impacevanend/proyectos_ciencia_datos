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
