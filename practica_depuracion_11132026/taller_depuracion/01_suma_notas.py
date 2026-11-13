# Objetivo: sumar todas las notas de la lista.
notas: list[int] = [7, 4, 9, 6]
total: int = 0
for i in range(len(notas) + 1):
    total: int = total + notas[i]
print("Suma:", total)
