piezas_capturadas: list[str] = ["Peon", "Caballo"]
turnos: list[int] = [3, 7]

print(f"{"Pieza":<10}|{"Turno":>5}")

for indice in range(len(piezas_capturadas)):
    pieza: str = piezas_capturadas[indice]
    turno: int = turnos[indice]

    print(f"{pieza:<10}|{turno:>5}")