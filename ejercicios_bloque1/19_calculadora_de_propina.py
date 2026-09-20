"""
Ejercicio Bloque 1: Fundamentos de Programación
Programa para calcular el valor total de una cuenta
incluyendo la propina deseada.
"""

importe: float = float(input("Valor de la cuenta: "))
propina: int = int(input("Ingresa el % de propina que quieres dar (0, 5, 10, 15): "))
importe_propina: float = (importe * propina / 100)

total: float = importe + importe_propina 

print("===Super Restaurant Elche===")
print(f"Importe: {importe:.2f}")
print(f"Propina ({propina}%): {importe_propina:.2f}")
print(f"Total: {total:.2f}")
print("===Gracias por tu visita===")