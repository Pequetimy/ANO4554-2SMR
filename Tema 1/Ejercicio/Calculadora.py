x = int(input("Introduce un operador:"))
y = int(input("Introduce un operador:"))
z = input("Introduce un operador +:")

print(f"{x} {z} {y} es: { {"+": x + y, "-": x - y, "*": x * y, "/": x / y,}[z]}")
