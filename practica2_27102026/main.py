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

def calcular_envio(importe_compra: float, importe_minimo: float = 50) -> float:
    """
    Calcula el coste del envio
    """
    if importe_compra >= importe_minimo:
        return 0.0
    else:
        return 4.95

print(f"Total envío: {calcular_envio(importe_compra = 30)}")
print(f"Total envío: {calcular_envio(importe_compra = 75)}")
print(f"Total envío: {calcular_envio(importe_compra = 30, importe_minimo = 25)}")