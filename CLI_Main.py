import CLI_Menus as menu
import CLI_Logica as logica
def main():
    while True:
        menu.menu_inicial()
        opciones = logica.obtener_opciones()
        if opciones == 1:
            datos = menu.menu_registro()
            logica.crear_archivo("Usuarios.json", datos)
        elif opciones == 2:
            print("Registro exitoso")
        elif opciones == 3:
            print("Saliendo...")
            break

main()



