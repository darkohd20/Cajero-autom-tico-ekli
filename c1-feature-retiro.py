saldo = 1000

menu = int(input("Opcion de retiro ingrse 2: "))

if menu == 2:
    monto = float(input("ingrese valor a retirar: "))
    saldo = saldo - monto
    print(f"Operacion exitosa su salgo actual es {saldo}.")