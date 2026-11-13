# Objetivo: quitar de la lista todas las notas suspensas (menores que 5).
notas: list[int] = [3, 4, 8, 2, 9]
for nota in notas:
    if nota < 5:
        notas.remove(nota)
print(notas)
