
def menu_inicial():
    # Funcion de presentacion solo textual de las comandos
    "Bienvenido a TareaManager(TM) la mejor aplicación para gestionar tus tareas sin impedimentos."
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")

def menu_login():
    # Funcion de presentacion solo textual de inicio de sesion
    "Ingrese su nombre y contraseña de usuario"
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    return username and password

def mostrar_menu():
    # Funcion de ejecucion de los menus
    menu_inicial()