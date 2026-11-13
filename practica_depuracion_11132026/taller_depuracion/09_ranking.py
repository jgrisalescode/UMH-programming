# Objetivo: guardar un ranking con una línea por jugador.
def guardar(nombre: str, puntos: int) -> None:
    with open("ranking.txt", "a") as fichero:
        fichero.write(nombre + "," + str(puntos) + "\n")


guardar("ana", 10)
guardar("luis", 7)
with open("ranking.txt", "r") as fichero:
    print(fichero.read())
