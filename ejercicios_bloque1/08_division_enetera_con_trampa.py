total_minutos: int = 165
horas = total_minutos // 60
minutos = total_minutos % 60

print(f"{horas} horas\n{minutos} minutos")

total_minutos = -165
horas = total_minutos // 60
minutos = total_minutos % 60

print(f"{horas} horas\n{minutos} minutos")

# Python no redondea a cero como lo hacen otros sistemas
# Por eso el valor esperado de -165 // 60 de -2 no se da
# Al python redondear hacia menos infinito el valor es -3
# Con esto se grantiza que (a // b) * b + (a % b) == a

# Demostración de esta garantía matemática del lenguaje.
print((total_minutos // 60) * 60 + (total_minutos % 60))