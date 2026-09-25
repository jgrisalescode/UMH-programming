vocales: str = "aeiou"
palabra: str = input("Ingresa una palabra: ")

total_vocales: int = 0

for letra in palabra:
    if letra in vocales:
        total_vocales += 1

print(f"La paralabra '{palabra}' tiene {total_vocales} vocales")