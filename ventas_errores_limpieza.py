# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:10:50 2024

@author: luis.bravo
"""

import pandas as pd


# Cargar el archivo CSV de ventas con errores

df_ventas_erroneas = pd.read_csv('ventas_erroneas.csv')


# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df_ventas_erroneas.head())

# INSPECCIÓN DE DATOS

# Inspeccionar el DataFrame
print("\nInformación del DataFrame de ventas con erroneas:")
print(df_ventas_erroneas.info())

print("\nDescripción estadística del DataFrame de ventas con errores:")
print(df_ventas_erroneas.describe(include='all'))
