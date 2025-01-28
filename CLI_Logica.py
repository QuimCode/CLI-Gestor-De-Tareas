import json
import os

def obtener_opciones():
    while True:
        try:
            opciones_elejidas = int(input("Ingrese el numero de la opcion que desea:"))
            if opciones_elejidas in [1,2,3]:
                return opciones_elejidas
            else:
                print("Opcion no valida, solo elije entre los numeros 1,2,3")
        except ValueError:
            print("Debe ingresar un caracter numerico y no de otro tipo.")

def crear_archivo(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "r") as archivo:
            json.load(archivo)

            for item in contenido:
                if item["nombre_usuario"] == datos["nombre_usuario"]:
                    print("El usuario ya existe, elije otro nombre")
                    return
                
            contenido.append(datos)

    except FileNotFoundError:
        contenido = []

    with open(nombre_archivo, "w") as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)
        print("Registro exitoso")
        