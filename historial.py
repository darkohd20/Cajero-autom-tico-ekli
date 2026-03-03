historial = []

def registrar(tipo, monto, saldo):
    if monto is None:
        historial.append(f"{tipo} - saldo: ${saldo}")
    else:
        historial.append(f"{tipo} - monto: ${monto} - saldo: ${saldo}")

def mostrar():
    if len(historial) == 0:
        print("no hay operaciones registradas.")
        return

    print("\n===== historial =====")
    for i in range(len(historial)):
        print(f"{i+1}. {historial[i]}")