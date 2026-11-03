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


class Estudiante():
    """
    Clase que representa un Estudiante en el Centro Educativo
    """

    def __init__(self, nombre: str, edad: int, nota_media: float) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nota_media: float = nota_media

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota media: {self.nota_media}"


ana = Estudiante(nombre = "Ana", edad = 19, nota_media = 8.25)
carlos = Estudiante(nombre = "Carlos", edad = 21, nota_media = 7.2)
print(ana)
print(carlos)


class Vehiculo():
    """
    Representa un vehículo con su marca, modelo y kilometraje.
    """

    def __init__(self, marca: str, modelo: str, kilometros: int) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.kilometros: int = kilometros

    
    def mostrar_informacion(self) -> None:
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Kilometros: {self.kilometros}")


    def conducir(self, distancia: int) -> None:
        self.kilometros = self.kilometros + distancia


toyota = Vehiculo(marca = "Toyota", modelo = "Corolla", kilometros = 15000)
seat = Vehiculo(marca = "Seat", modelo = "Ibiza", kilometros = 8000)

toyota.mostrar_informacion()
seat.mostrar_informacion()

toyota.conducir(distancia = 2000)
seat.conducir(distancia = 150)

toyota.mostrar_informacion()
seat.mostrar_informacion()