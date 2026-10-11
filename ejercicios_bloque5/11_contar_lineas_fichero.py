path: str = "multiline.txt"

with open(path, "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
    file.write("Line 4")

with open(path, "r") as file:
    lines: list[str] = file.readlines()
    print(lines, len(lines))