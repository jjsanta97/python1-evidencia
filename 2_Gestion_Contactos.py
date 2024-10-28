class Contacto:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def mostrar_menu():
    print("Gestión de Contactos")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("")

contactos = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el teléfono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
        print("Contacto agregado")
        print("")
    elif opcion == "2":
        for c in contactos:
            print(f"{contactos.index(c) + 1}. Nombre: {c.nombre}, Teléfono: {c.telefono}")
            print("")
    elif opcion == "3":
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
                print("")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
            print("")
    elif opcion == "4":
        nombre = input("Ingresa el nombre del contacto a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado")
                print("")