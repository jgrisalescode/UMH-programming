# Objetivo: sumar las edades de una lista de textos, avisando de las que no sean válidas.
def convertir(texto: str) -> float:
    try:
        return float(texto)
    except:
        return 0


edades: list[str] = ["20", "19", "dieciocho", "21.5"]
total: float = 0
for texto in edades:
    total: float = total + convertir(texto)
print("Suma de edades:", total)
