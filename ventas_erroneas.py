import pandas as pd
import numpy as np

# Crear un DataFrame con muchos registros, incluyendo errores y valores nulos
np.random.seed(42)
num_records = 10000
data = {
    'Fecha': np.random.choice(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', 'Not a date', None], num_records),
    'Producto': np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', None], num_records),
    'Monto': np.random.choice(['100', '200', '300', '400', '500', 'not a number', None], num_records)
}

df_errores = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
file_path = 'ventas_erroneas.csv'
df_errores.to_csv(file_path, index=False)

file_path