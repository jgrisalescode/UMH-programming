movimiento: str = "e2e4"

origen: str = ""
destino: str = ""

if len(movimiento) == 4:
    origen = movimiento[:2]
    destino = movimiento[-2:]

print(origen, destino)