import pandas as pd
from models import Marca,Modelo

# Función para leer un archivo de Excel y convertirlo en un diccionario
def leer_excel(nombre):
    df = pd.read_excel(nombre)
    dic = df.to_dict("records")
    return dic

# Función para crear y guardar instancias de un modelo
def crear_modelo(modelo, datos):
    for dato in datos:
        codigo = dato["codigo"]
        descripcion = dato["descripcion"]
        # Si el modelo es Modelo, se necesita el campo marca
        if modelo == Modelo:
            marca = dato["marca"]
            obj = modelo(codigo=codigo, marca=marca, descripcion=descripcion)
        else:
            obj = modelo(codigo=codigo, descripcion=descripcion)
        obj.save()

# Leer los archivos de Excel
marcas = leer_excel("csv/marcas.xlsx")
modelos = leer_excel("csv/modelos.xlsx")

# Crear y guardar las instancias de los modelos
crear_modelo(Marca, marcas)
crear_modelo(Modelo, modelos)