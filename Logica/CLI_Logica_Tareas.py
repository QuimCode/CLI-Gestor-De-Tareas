def crear_tarea(usuario):
    usuario_actual = usuario
    print(f"Señor/ra {usuario_actual} porfavor creé su tarea, eliga un nombre, su descripcion y como ultimo eliga el horario estipulado para completar dicha tarea.")
    nombre_tarea = input("Como se llamara su tarea ? :")
    descripcion_tarea = input("Ingrese la descripcion de la tarea :")
    horario_tarea = input("Ingrese el horario para completar la tarea creada:")
    return {
        "Usuario": usuario_actual,
        "Nombre de la Tarea": nombre_tarea,
        "Descripcion de la Tarea": descripcion_tarea,
        "Horario de la Tarea": horario_tarea,
        "Tarea Terminada": False,
        "Tarea No Terminada": True,
        "Tarea No Vencida": True,
    }

