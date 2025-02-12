import json

def crear_tarea(usuario):
    usuario_actual = usuario
    print(f"Señor/ra {usuario_actual} porfavor creé su tarea, eliga un nombre, su descripcion y como ultimo eliga el horario estipulado para completar dicha tarea.")
    nombre_tarea = input("Como se llamara su tarea ? :")
    descripcion_tarea = input("Ingrese la descripcion de la tarea :")
    horario_tarea = input("Ingrese el horario para completar la tarea creada:")
    return {
        "usuario": usuario_actual,
        "nombre_de_tarea": nombre_tarea,
        "descripcion_de_tarea": descripcion_tarea,
        "horario_de_tarea": horario_tarea,
        "tarea_terminada": False,
        "tarea_no_terminada": True,
        "tarea_no_vencida": True,
    }

#====================================CREAR ARCHIVO====================================
ruta_carpeta = "Informacion/Tareas.json"

def crear_archivo_tarea(datos):
    try:
        with open(ruta_carpeta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

            for item in contenido:
                if item["nombre_de_tarea"] == datos["nombre_de_tarea"]:
                    print("Ya existe una tarea con ese nombre.")
                    return
                
            contenido.append(datos)

    except FileNotFoundError:
        contenido = []
        contenido.append(datos)

    with open(ruta_carpeta, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)
        print("Registro exitoso")

#====================================CREAR ARCHIVO====================================

def editar_tarea(usuario):
    usuario_actual = usuario
    print(f"Hola {usuario_actual} porfavor ingrese el nombre de la tarea que desea editar,")
    nombre_tarea = input("Nombre de la tarea a editar:")
    try:
        pass
    except:
        pass

def listar_tarea(usuario):
    usuario_actual = usuario
    print(f"Estas son sus tareas usuario {usuario_actual}")
    try:
        with open(ruta_carpeta, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            for item in contenido:
                if item["usuario"] == usuario_actual:
                    print(f"Tarea: {item['nombre_de_tarea']}")
                    print(f"Descripcion: {item['descripcion_de_tarea']}")
                    print(f"Horario: {item['horario_de_tarea']}")
                    print(f"Tarea terminada: {item['tarea_terminada']}")
                    print(f"Tarea no terminada: {item['tarea_no_terminada']}")
                    print(f"Tarea no vencida: {item['tarea_no_vencida']}")
                    print("")
    except FileNotFoundError:
        print("No hay tareas creadas")