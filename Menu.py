def menu():
    print("\n--- Menu Ñekli ---")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

while True:
    try:
        operaciones = int(input("Cuántas operaciones desea realizar?: "))
        

        if operaciones <= 0:
            print("Debe ingresar un número válido")
        else:
            break

    except ValueError:
        print("Eso no es un número, inténtelo otra vez")