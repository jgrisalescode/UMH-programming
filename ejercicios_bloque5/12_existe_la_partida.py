import os

ruta: str = "partida_guardada.txt"

if os.path.exists(ruta):
    print(f"Existe el fichero: {ruta}")
else:
    print(f"El fichero: {ruta} no existe")