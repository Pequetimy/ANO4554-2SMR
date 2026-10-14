#Ejemplo4-2.py
x = int(input("Introduce un número:"))
y = int(input("Introduce un número:"))
opr = input("Introduce un operador (+, -, *, /, //):")
#Funcióne val() =
resultado = eval(f"{x} {opr} {y}")

print(f"Resultado: {resultado}")