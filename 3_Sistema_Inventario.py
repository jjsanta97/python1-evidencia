class Producto:

    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


def mostrar_menu():
    print("Sistema de Inventario")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("")


inventario = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "6":
        print("Saliendo del programa")
        break

    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado")
            print("")
        except ValueError:
            print("Error: Entrada no válida")
            print("")
    elif opcion == "2":
        for p in inventario:
            print(f"{inventario.index(p) + 1}. Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        print("")
    elif opcion == "3":
        nombre = input("Ingresa el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
                print("")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")
            print("")
    elif opcion == "4":
        nombre = input("Ingresa el nombre del producto a actualizar: ")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad = nueva_cantidad
                    print("Cantidad actualizada")
                    print("")
                    break
        except ValueError:
            print("Error: Entrada no válida")
            print("")
    elif opcion == "5":
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado")
                print("")
