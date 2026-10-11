piezas_capturadas: list[dict[str, str]] = [
    {"turno": "1", "color": "blancas", "pieza": "Peón"},
    {"turno": "2", "color": "negras", "pieza": "Caballo"},
    {"turno": "3", "color": "blancas", "pieza": "Alfil"},
    {"turno": "4", "color": "negras", "pieza": "Peón"},
    {"turno": "5", "color": "blancas", "pieza": "Torre"},
    {"turno": "6", "color": "negras", "pieza": "Dama"},
    {"turno": "7", "color": "blancas", "pieza": "Caballo"},
    {"turno": "8", "color": "negras", "pieza": "Alfil"},
    {"turno": "9", "color": "blancas", "pieza": "Peón"},
    {"turno": "10", "color": "negras", "pieza": "Torre"},
]

count: int = 0

for pieza in piezas_capturadas:

    if pieza["color"] == "blancas":
        count += 1
    
    print(f"Turno: {pieza["turno"]} <{pieza["color"]}> <{pieza["pieza"]}>")

print(f"Total piezas blancas capturadas: {count}")