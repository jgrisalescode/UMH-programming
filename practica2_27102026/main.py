def calcular_total(precio: float, entradas: int) -> float:
    """
    Calcula el total de las entradas.

    Args:
        precio (float): Precio entradas.
        entradas (int): Cantidad entradas.

    Returns:
        float: total de las entradas.
    """
    return entradas * precio

print(calcular_total(entradas=4, precio=7.5))