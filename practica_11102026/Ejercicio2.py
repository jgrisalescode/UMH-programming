inventario: dict[str, int] = {
    "teclado": 8,
    "raton": 3,
    "monitor": 0,
    "auriculares": 5,
    "webcam": 2
}


def analizar_inventario(inventario: dict[str, int]) -> tuple[int, list[str]]:
    """
    Funcion que analiza el bajo stock en un alamacén
    """
    total: int = 0
    stock_bajo: list[str] = []

    for producto, cantidad in inventario.items():
        total = total + cantidad

        if cantidad < 4:
            stock_bajo.append(producto)

    return total, stock_bajo

reporte: tuple[int, list[str]] = analizar_inventario(inventario = inventario)
print(f"Unidades totales: {reporte[0]}\nProductos bajos: {reporte[1]}")