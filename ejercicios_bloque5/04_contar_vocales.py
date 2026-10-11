palabra: str = "mUrCiElAgo"
count: int = 0

for letra in palabra.lower():
    if letra in "aeiou":
        count += 1

print(f"La palabra {palabra} tiene: {count} vocales")
