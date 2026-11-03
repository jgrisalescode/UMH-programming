class Animal():
    """
    Clase que representa un animal
    """

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad


    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Perro(Animal):
    """
    Clase que representa un perro
    """

    def ladrar(self) -> None:
        print("Woof woof")


class Gato(Animal):
    """
    Clase para representar un gato
    """

    def maullar(self) -> None:
        print("Miau")


rocco = Perro("Rocco", 3)
rocco.mostrar_informacion()
rocco.ladrar()
misu = Gato("Misu", 2)
misu.mostrar_informacion()
misu.maullar()
