import pandas as pd
import json
import os 
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
ruta_de_modelos = os.path.join(DIRECTORIO_ACTUAL, 'modelos.xls')
ruta_de_marcas  = os.path.join(DIRECTORIO_ACTUAL, 'marcas.xls')
# leer archivo xls
df = pd.read_excel(ruta_de_marcas)


# convertir DataFrame a diccionario
data = df.to_dict(orient='records')

# escribir datos en archivo json
with open('marcas.json', 'w') as f:
    if f:
        print("El archivo se ha creado correctamente.")
    else:
        print("Error al crear el archivo.")
    json.dump(data, f)


modelos = pd.read_excel(ruta_de_modelos)

data2 = modelos.to_dict(orient='records')

with open('modelos.json', 'w') as f:
    if f:
        print("El archivo se ha creado correctamente.")
    else:
        print("Error al crear el archivo.")
    json.dump(data2, f)
    

