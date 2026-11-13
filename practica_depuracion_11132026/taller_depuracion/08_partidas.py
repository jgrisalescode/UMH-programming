# Objetivo: cada partida anota SUS propios movimientos.
class Partida:
    movimientos: list[str] = []

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre

    def anotar(self, movimiento: str) -> None:
        self.movimientos.append(movimiento)


p1: Partida = Partida("p1")
p2: Partida = Partida("p2")
p1.anotar("e2 e4")
p2.anotar("d2 d4")
print(p1.nombre, p1.movimientos)
print(p2.nombre, p2.movimientos)
