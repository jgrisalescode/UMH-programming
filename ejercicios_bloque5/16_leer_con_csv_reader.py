import csv

path: str = "historial.csv"

with open(path, "w") as file:
    file.write("turno,color,pieza\n")
    file.write("3,blancas,Peon\n")
    file.write("7,negras,Caballo")

with open(path, "r") as file:
    lector = csv.reader(file)

    for linea in lector:
        print(linea)