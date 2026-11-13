# Objetivo: preguntar si se quiere jugar otra partida; solo "s" o "S" significan que sí.
respuesta: str = input("¿Otra partida? (s/n): ")
# if respuesta == "s" or respuesta == "S":
if respuesta.lower() == "s":
    print("Nueva partida")
else:
    print("Adiós")
