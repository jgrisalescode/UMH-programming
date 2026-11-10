def procesar_producto(texto: str) -> tuple[str, float]:
    """Devuelve el nombre y precio de un producto"""

    partes: list[str] = texto.split(sep = ",")

    if len(partes) != 2:
        return "", -1.0
   
    producto: str = partes[0].upper()

    try:
        precio: float = float(partes[1])
    except:
        return "", -1.0

    return producto, precio


print(procesar_producto("Teclado,45"))
print(procesar_producto("Raton,20"))
print(procesar_producto("Monitor"))
print(procesar_producto("Monitor,Raton"))