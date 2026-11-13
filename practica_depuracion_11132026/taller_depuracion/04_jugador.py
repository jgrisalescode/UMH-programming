# Objetivo: guardar el nombre y los puntos de un jugador y saludarlo.
class Jugador:
    def __init__(self, nombre: str, puntos: int) -> None:
        nombre: str = nombre
        self.puntos: int = puntos

    def saludar(self) -> str:
        return "Hola, " + self.nombre


jugador: Jugador = Jugador("ana", 10)
print(jugador.puntos)
print(jugador.saludar())
