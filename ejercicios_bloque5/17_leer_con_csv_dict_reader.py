import csv

path: str = "historial.csv"

with open(path, "r", newline="") as file:
    lector = csv.DictReader(file)

    for linea in lector:
        print(f"{linea["pieza"]} {linea["color"]} capturada en el turno {linea["turno"]}")