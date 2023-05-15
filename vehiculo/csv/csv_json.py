import pandas as pd
import json

# leer archivo xls
df = pd.read_excel('C:/Users/acer/OneDrive/Escritorio/program/trabajo/vehiculo/csv/marcas.xls')

# convertir DataFrame a diccionario
data = df.to_dict(orient='records')

# escribir datos en archivo json
with open('marcas.json', 'w') as f:
    if f:
        print("El archivo se ha creado correctamente.")
    else:
        print("Error al crear el archivo.")
    json.dump(data, f)


modelos = pd.read_excel('C:/Users/acer/OneDrive/Escritorio/program/trabajo/vehiculo/csv/modelos.xls')

data2 = modelos.to_dict(orient='records')

with open('modelos.json', 'w') as f:
    if f:
        print("El archivo se ha creado correctamente.")
    else:
        print("Error al crear el archivo.")
    json.dump(data2, f)
    

