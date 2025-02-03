import Logica.CLI_Logica as logica

def menu_inicial():
    # Funcion de presentacion solo textual de las comandos
    "Bienvenido a TareaManager(TM) la mejor aplicación para gestionar tus tareas sin impedimentos."
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_registro():
    datos_usuario = logica.registrarse()
    return datos_usuario

def mostrar_menu():
    # Funcion de ejecucion de los menus
    menu_inicial()