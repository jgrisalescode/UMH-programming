"""
Ejercicios Bloque 1: Fundamentos de Programación
Simulamos la lista de la compra
"""

verduras: float = float(input("Precio de las verduras: "))
frutas: float = float(input("Precio de las frutas: "))
carnes: float = float(input("Precio de las carnes: "))

total_compra: float = verduras + frutas + carnes

# {total_compra:.2f} presenta el valor total con 2 dígitos en la parte decimal.
print(f"Total compra: {total_compra:.2f}€")