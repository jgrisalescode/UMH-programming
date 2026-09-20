import sys

small_integer: int = 5
big_integer: int = 10 ** 50
string_size: str = "My name is Carlos Julian Grisales Alvarez"

print(sys.getsizeof(small_integer))
print(sys.getsizeof(big_integer))
print(sys.getsizeof(string_size))

# Es notable el consumo de bits de la cadena de texto conparada incluso
# con un número grande