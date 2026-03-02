usuario_autenticacion = "David"

usuario =input ("ingrese usuario: ")


def control_intentos():
    usuario_autenticacion = "David"

    for i in range(3):
        pin = input("Ingrese PIN: ")
        
        if pin.lower() == usuario_autenticacion.lower():
            print("PIN Correcto.")
            break
        else:
            print(f"Error, PIN incorrecto. Intento: {i + 1}")
    else:
        print("No tiene más intentos.")