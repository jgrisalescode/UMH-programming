high: float = float(input("Ingrea tu altura en metros, por ejemplo 1.73: "))

high = int(high)

print(high) # Output 1, hemos truncado la parte decimal

high = float(high) # Si devolvemos el proceso

print(high) # Confirmamos que la parte decimal la hemos perdido

# Hay que tener mucho cuidado con este tipo de casting ya que podemos perder datos.