import Menu.CLI_Menus as menu
import Logica.CLI_Logica as logica
def main():
    while True:
        # menu.menu_inicial()
        # opciones = logica.obtener_opciones()
        # if opciones == 1:
        #     datos = menu.menu_registro()
        #     logica.crear_archivo("Usuarios.json", datos)
        # elif opciones == 2:
        #     logica.iniciar_sesion()
        # elif opciones == 3:
        #     print("Saliendo...")
        #     break
        logica.interacion_menu()
        logica.interacion_menu_app()

main()

