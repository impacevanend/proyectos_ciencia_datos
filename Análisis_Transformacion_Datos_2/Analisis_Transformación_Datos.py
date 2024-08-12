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