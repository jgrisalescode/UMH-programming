numero: int = 25
en_rango: bool = numero >= 1 and numero <= 100

print(f"El número: {numero} esta entre 1 y 100: {en_rango}")

numero = 999
en_rango = numero >= 1 and numero <= 100

print(f"El número: {numero} esta entre 1 y 100: {en_rango}")