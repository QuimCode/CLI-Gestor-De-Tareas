import Menu.CLI_Menus as menu
import Logica.CLI_Logica as logica

def main():
    while True:
        if not logica.interacion_menu():
            break

main()

