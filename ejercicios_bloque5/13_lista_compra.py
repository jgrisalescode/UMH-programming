compra: list[str] = ["frutas", "verduras", "carnes", "lácteos"]
fichero: str = "compra.txt"

with open(fichero, "w") as file:
    for item in compra:
        file.write(f"{item}\n")

with open(fichero, "r") as file:
    for item in file:
        print(item, end="")