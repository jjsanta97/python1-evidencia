class Tarea:

    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado


def mostrar_menu():
    print("Sistema de Gestión de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Buscar tarea")
    print("4. Filtrar tarea por estado (Activa/Inactiva)")
    print("5. Actualizar tarea")
    print("6. Eliminar tarea")
    print("7. Salir")
    print("")


tareas = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "7":
        print("Saliendo del programa")
        break

    if opcion == "1":
        try:
            titulo = input("Ingresa el título de la tarea: ")
            descripcion = input("Ingrese la descripcion: ")
            estado = input("Ingrese el estado: ")
            tarea = Tarea(titulo, descripcion, estado)
            tareas.append(tarea)
            print("Tarea agregada")
            print("")
        except ValueError:
            print("Error: Entrada no válida")
            print("")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas para mostrar")
            print("")
        else:
            for t in tareas:
                print(f"{tareas.index(t) + 1}. Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
            print("")
    elif opcion == "3":
        titulo = input("Ingresa el título de la tarea a buscar: ")
        encontrado = False
        for t in tareas:
            if t.titulo.lower() == titulo.lower():
                print(f"{tareas.index(t) + 1}. Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
                print("")
                encontrado = True
                break
        if not encontrado:
            print("Tarea no encontrado")
            print("")
    elif opcion == "4":
        estado = input("Ingresa el estado de las tareas a filtrar: ")
        if estado == "Activa":
            for t in tareas:
                if t.estado == "Activa":
                    print(f"{tareas.index(t) + 1}. Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
            print("")
        elif estado == "Inactiva":
            for t in tareas:
                if t.estado == "Inactiva":
                    print(f"{tareas.index(t) + 1}. Título: {t.titulo}, Descripción: {t.descripcion}, Estado: {t.estado}")
            print("")
        else:
            print("Ingresa un estado válido (Activa o Inactiva)")
    elif opcion == "5":
        nombre = input("Ingresa el título de la tarea a actualizar: ")
        try:
            nueva_descripcion = input("Ingrese la nueva descripcion: ")
            for t in tareas:
                if t.titulo.lower() == titulo.lower():
                    t.descripcion = nueva_descripcion
                    print("Descripcion actualizada")
                    print("")
                    break
        except ValueError:
            print("Error: Entrada no válida")
            print("")
    elif opcion == "6":
        nombre = input("Ingresa el titulo de la tarea a eliminar: ")
        for t in tareas:
            if t.titulo.lower() == titulo.lower():
                tareas.remove(t)
                print("Tarea eliminado")
                print("")
