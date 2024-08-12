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

#2. Aplicación de funciones: 'apply' y 'map'

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

#3. Combinación de DataFrames: merge y concat


# CREAR DATAFRAME SIMULADO DE PRODUCTOS
data_categorias = {'Producto':['A','B','C','D'],
                   'Categoría':['Electrónica', 'Ropa', 'Hogar', 'Deportes']}

df_categorias = pd.DataFrame(data_categorias)

# Mostrar el dataFrame de categorías

print(df_categorias)

# paso 2 combinar los dataFrame
# Unir los DataFrames en base a la columna 'Producto'

df_combinado = pd.merge(df_ventas, df_categorias, on='Producto', how='left')

# Mostrar las primeras filas del DataFrame combinado
print(df_combinado.head())

# 4. Calcular Estadísticas Básicas: Media, Mediana, Moda

# Calcular la media del monto
media_monto = df_ventas['Monto'].mean()
print(f"Media del monto: {media_monto}")

# Calcular la mediana del monto
mediana_monto = df_ventas['Monto'].median()
print(f"Mediana del monto: {media_monto}")

# Calcula la moda del monto
moda_monto = df_ventas['Monto'].mode()
print(f"Moda del monto: {moda_monto[0]}") 



