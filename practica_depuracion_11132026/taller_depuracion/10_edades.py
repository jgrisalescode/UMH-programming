# Objetivo: sumar las edades de una lista de textos, avisando de las que no sean válidas.
def convertir(texto: str) -> int:
    try:
        return int(texto)
    except:
        return 0


edades: list[str] = ["20", "19", "dieciocho", "21.5"]
total: int = 0
for texto in edades:
    total: int = total + convertir(texto)
print("Suma de edades:", total)
