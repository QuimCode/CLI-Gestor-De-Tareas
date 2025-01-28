
def menu_inicial():
    # Funcion de presentacion solo textual de las comandos
    "Bienvenido a TareaManager(TM) la mejor aplicación para gestionar tus tareas sin impedimentos."
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_registro():
    # Funcion de presentacion solo textual de inicio de sesion
    "Ingrese su nombre y contraseña para registrarse"
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    return {
        "username": username,
        "password": password
    }

def mostrar_menu():
    # Funcion de ejecucion de los menus
    menu_inicial()