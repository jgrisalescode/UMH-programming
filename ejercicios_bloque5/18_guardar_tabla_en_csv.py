import csv

piezas_capturadas: list[dict[str, str]] = [
    {"turno": "1", "color": "blancas", "pieza": "Peon"},
    {"turno": "2", "color": "negras", "pieza": "Caballo"},
    {"turno": "3", "color": "blancas", "pieza": "Alfil"},
    {"turno": "4", "color": "negras", "pieza": "Peon"},
    {"turno": "5", "color": "blancas", "pieza": "Torre"},
    {"turno": "6", "color": "negras", "pieza": "Dama"},
    {"turno": "7", "color": "blancas", "pieza": "Caballo"},
    {"turno": "8", "color": "negras", "pieza": "Alfil"},
    {"turno": "9", "color": "blancas", "pieza": "Peon"},
    {"turno": "10", "color": "negras", "pieza": "Torre"},
]

cabecera: list[str] = ["turno", "color", "pieza"]

path: str = "capturas.csv"

with open(path, "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=cabecera)
   writer.writeheader()

   for captura in piezas_capturadas:
      writer.writerow(captura)

with open(path, "r", newline="") as file:
   reader = csv.DictReader(file)
   for line in reader:
      print(line["turno"],line["color"],line["pieza"])