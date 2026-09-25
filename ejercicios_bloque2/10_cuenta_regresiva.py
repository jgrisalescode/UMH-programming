import time

cuenta_regresiva: int = 10

print("T-Minus")

while cuenta_regresiva > 0:
    print(cuenta_regresiva)
    cuenta_regresiva -= 1
    time.sleep(1)

print("Despegue! \U0001F680")