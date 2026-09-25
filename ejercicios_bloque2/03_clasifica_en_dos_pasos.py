fila: int = 5
columna: int = 5

if fila >= 0:
    if fila <= 7:
        print(f"Fila: {fila}")
        if columna >= 0:
            if columna <= 7:
                print(f"Columna: {columna}")
            else:
                print("Columan inválida")
        else:
            print("Columan inválida")
    else: 
        print("Fila inválida")
else:
    print("Fila inválida")
