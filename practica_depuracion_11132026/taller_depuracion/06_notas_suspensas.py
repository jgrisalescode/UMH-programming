# Objetivo: quitar de la lista todas las notas suspensas (menores que 5).
notas: list[int] = [3, 4, 8, 2, 9]
suspensos: list[int] = []
aprobados: list[int] = []
for nota in notas:
    if nota < 5:
        suspensos.append(nota)
    else:
        aprobados.append(nota)
print(aprobados)
