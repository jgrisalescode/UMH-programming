with open("saludo.txt", "w") as file:
    file.write("Hola desde un fichero\n")

with open("saludo.txt", "r") as file:
    content: str = file.read()
    print(content)