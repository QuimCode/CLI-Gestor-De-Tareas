import json
import os
import Menu.CLI_Menus as menu

#====================================MENU====================================
opciones_validas_menu = [1,2,3]
opciones_validas_menu_app = [1,2,3,4,5,6,7,8]


def obtener_opciones(opciones_correctas):
    while True:
        try:
            opciones_elejida = int(input("Ingrese el numero de la opcion que desea:"))
            if opciones_elejida in opciones_correctas:
                return opciones_elejida
            else:
                print("Opcion no valida, solo elije entre los numeros 1,2,3")
        except ValueError:
            print("Debe ingresar un caracter numerico y no de otro tipo.")

def interacion_menu():
    while True:
        menu.menu_inicial()
        opciones = obtener_opciones(opciones_validas_menu)
        if opciones == 1:
            datos = menu.menu_registro()
            crear_archivo("Usuarios.json", datos)
        elif opciones == 2:
            if iniciar_sesion():
                return True
        elif opciones == 3:
            print("Saliendo...")
            return False

def interacion_menu_app():
    while True:
        menu.menu_app()
        opciones = obtener_opciones(opciones_validas_menu_app)
        if opciones == 1:
            print("Crear tarea")
        elif opciones == 2:
            print("Editar tarea")
        elif opciones == 3:
            print("Eliminar tarea")
        elif opciones == 4:
            print("Listar tareas terminadas")
        elif opciones == 5:
            print("Listar tareas pendientes")
        elif opciones == 6:
            print("Listar tareas no terminadas")
        elif opciones == 7:
            print("Listar todas las tareas")
        elif opciones == 8:
            print("Volver al menu principal")            
            # menu.menu_inicial()
            return False

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
        with open(ruta_carpeta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

            for item in contenido:
                if item["dato_nombre"] == nombre_de_usuario and item["dato_clave"] == contraseña:
                    print(f"Bienvenido {nombre_de_usuario}")
                    interacion_menu_app()
                    return True
                else:
                    print("Usuario o contraseña incorrectos o usuarios no registrado.")
    
    except FileNotFoundError:
        print("No hay usuarios registrados")