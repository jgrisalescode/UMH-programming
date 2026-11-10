def analizar_notas(notas: list[float]) -> tuple[float | None, int]:
    """
    Calcula la nota media de notas y el total de estudiantes que aprobaron
    """
    suma: float = 0
    aprobados: int = 0

    if len(notas) == 0:
        return None, 0

    for nota in notas:
        suma = suma + nota

        if nota >= 5:
            aprobados += 1        

    return round(suma / len(notas), 2), aprobados


notas: list[float] = [7.5, 4.0, 8.2, 5.0, 9.1, 3.5]
print(analizar_notas(notas = notas))

notas_vacia: list[float] = []
print(analizar_notas(notas = notas_vacia))