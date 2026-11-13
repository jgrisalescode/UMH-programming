# Objetivo: calcular la media de una lista y sumarle un punto extra.
def media(valores: list[int]) -> float:
    total: int = sum(valores)
    resultado: float = total / len(valores)
    print(resultado)


nota: float = media([6, 8, 10])
print("Con punto extra:", nota + 1)
