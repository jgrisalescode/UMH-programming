# Objetivo: sumar todas las notas de la lista.
notas: list[int] = [7, 4, 9, 6]
total: int = 0
for nota in notas:
    total: int = total + nota
print("Suma:", total)
