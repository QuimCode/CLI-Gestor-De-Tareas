import Logica.CLI_Logica as logica
import Logica.CLI_Logica_Tareas as log_tareas

def mostrar_menu():
    # Funcion de ejecucion de los menus
    menu_inicial()

def menu_inicial():
    # Funcion de presentacion solo textual de las comandos
    "Bienvenido a TareaManager(TM) la mejor aplicación para gestionar tus tareas sin impedimentos."
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_registro():
    datos_usuario = logica.registrarse()
    return datos_usuario

def menu_app():
    # Funcion de presentacion solo textual de las comandos
    print("1. Crear tarea")
    print("2. Editar tarea")
    print("3. Eliminar tarea")
    print("4. Listar tareas terminadas")
    print("5. Listar tareas pendientes")
    print("6. Listar tareas no terminadas")
    print("7. Listar todas las tareas")
    print("8. Volver al menu principal")


def menu_registro_tarea(usuario):
    datos_tarea = log_tareas.crear_tarea(usuario) #Falta pasar de alguna forma el argumento de nombre de usuario
    return datos_tarea