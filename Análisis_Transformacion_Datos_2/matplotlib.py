import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df_ventas = pd.read_csv('ventas_erroneas.csv')

# Mostrar las primeras filas para asegurarnos de que datos se cargaron correctamente
print(df_ventas.head())
# Crear un gráfico de barras para ver la distribución de los productos vendidos
df_ventas['Producto'].value_counts().plot(kind='bar')

# Añadir titulos y etiquetas:
ax = df_ventas['Producto'].value_counts().plot(kind='bar')    
ax.set_title('Distribución de Productos Vendidos')
ax.set_xlabel('Producto')
ax.set_ylabel('Cantidad Vendida')


# Mostrar el gráfico
plt.show()