class Producto():
    """
    Representa un producto del catálogo con su precio y cantidad disponible.

    Esta clase almacena la información básica de un producto para
    su gestión en inventario o venta.

    Atributos:
        nombre (str):   Nombre del producto
        precio (float): Precio unitario del producto.
        cantidad (int): Número de unidades disponibles del producto.
    """

    def __init__(self, nombre: str, precio: float, cantidad: int) -> None:
        self.nombre: str = nombre
        self.precio: float = precio
        self.cantidad: float = cantidad


    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: {self.precio}€, Cantidad: {self.cantidad}"


ordenador = Producto(nombre = "Ordenador", precio = 800, cantidad = 2)
raton = Producto(nombre = "Ratón", precio = 25, cantidad = 5)
print(ordenador)
print(raton)

