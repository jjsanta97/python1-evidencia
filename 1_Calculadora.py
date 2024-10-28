def mostrar_menu():
    print("Calculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("")


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error: El divisor no puede ser 0"
    else:
        return num1 / num2


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Saliendo del programa")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {suma(num1, num2)}")
        print("")
    elif opcion == "2":
        print(f"Resultado: {resta(num1, num2)}")
        print("")
    elif opcion == "3":
        print(f"Resultado: {multiplicacion(num1, num2)}")
        print("")
    elif opcion == "4":
        print(f"Resultado: {division(num1, num2)}")
        print("")
