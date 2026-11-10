def resumir_notas(notas: list[float]) -> tuple[float, int]:
    
    if len(notas) == 0:
        return 0.00, 0

    suma: float = 0.0
    aprobados: int = 0

    for nota in notas:
        suma += nota

        if nota >= 5:
            aprobados += 1

    media: float = suma / len(notas)

    return media, aprobados


notas: list[float] = [4.0, 7.0, 5.0, 8.0]

media, aprobados = resumir_notas(notas = notas)
print(f"Media: {media:.2f}")
print(f"Aprobados: {aprobados}")