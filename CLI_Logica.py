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


