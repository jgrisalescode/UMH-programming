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


def es_casilla_valida(casilla: str) -> bool:
    """
    Devuleve la validacion de una casilla
    """
    letras: str = "abcdefgh"
    numeros: str = "12345678"

    if len(casilla) != 2:
        return False

    if casilla.lower()[0] not in letras:
        return False

    if casilla.lower()[1] not in numeros:
        return False

    return True

print(f"e2 es casilla valida: {es_casilla_valida("e2")}")
print(f"h8 es casilla valida: {es_casilla_valida("h8")}")
print(f"z4 es casilla valida: {es_casilla_valida("z4")}")
print(f"a9 es casilla valida: {es_casilla_valida("a9")}")