verduras: float = float(input("Precio de las verduras: "))
frutas: float = float(input("Precio de las frutas: "))
carnes: float = float(input("Precio de las carnes: "))

total_compra: float = verduras + frutas + carnes

print(f"Total compra: {total_compra:.2f}€")