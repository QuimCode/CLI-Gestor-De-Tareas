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

#====================================REGISTRO & Y LOGUEO====================================

carpeta = "Informacion/Usuarios.json"
ruta_carpeta = os.path.join(carpeta,)

def registrarse():
    # Funcion de presentacion solo textual de inicio de sesion
    "Ingrese su nombre y contraseña para registrarse"
    nombre_usuario = input("Nombre de usuario: ")
    contraseña_usuario = input("Contraseña: ")
    return {
        "dato_nombre": nombre_usuario,
        "dato_clave": contraseña_usuario
    }

def crear_archivo(nombre_archivo, datos):

    try:
        with open(ruta_carpeta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

            for item in contenido:
                if item["dato_nombre"] == datos["dato_nombre"]:
                    print("El usuario ya existe, elije otro nombre")
                    return
                
            contenido.append(datos)

    except FileNotFoundError:
        contenido = []
        contenido.append(datos)
        

    with open(ruta_carpeta, "w") as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)
        print("Registro exitoso")

def iniciar_sesion():
    nombre_de_usuario = input("Ingrese Nombre de usuario:")
    contraseña = input("Ingrese Contraseña:")

    try:
        with open(ruta_carpeta, "r") as archivo:
            contenido = json.load(archivo)

            for item in contenido:
                if item["dato_nombre"] == nombre_de_usuario and item["dato_clave"] == contraseña:
                    print(f"Bienvenido {nombre_de_usuario}")
    
    except FileNotFoundError:
        print("No hay usuarios registrados")