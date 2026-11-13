# Objetivo: preguntar si se quiere jugar otra partida; solo "s" o "S" significan que sí.
respuesta: str = input("¿Otra partida? (s/n): ")
if respuesta == "s" or "S":
    print("Nueva partida")
else:
    print("Adiós")
