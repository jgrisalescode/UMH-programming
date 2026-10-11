linea: str = "Torre,blanca,a1"
linea_lista: list[str] = linea.split(",")

nombre: str = linea_lista[0]
color: str = linea_lista[1]
casilla: str = linea_lista[2]

print(f"Nombre: {nombre}, Color: {color}, Casilla: {casilla}")

linea_reconstruida: str = ",".join(linea_lista)

print(linea_reconstruida)