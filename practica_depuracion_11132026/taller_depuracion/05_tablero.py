# Objetivo: tablero 3x3 de ceros con un 1 solo en la esquina superior izquierda.
tablero: list[list[int]] = [[0] * 3] * 3
tablero[0][0] = 1
for fila in tablero:
    print(fila)
