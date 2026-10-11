ruta: str = "notas.txt"

with open(ruta, "w") as file:
    file.write("Task 1\n")

with open(ruta, "a") as file:
    file.write("Task 2\n")
    file.write("Task 3\n")
    file.write("Task 4\n")