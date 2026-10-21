x = int(input("Introduce un número:"))
y = int(input("Introduce otro número:"))
z = input("Introduce un operador +, -, *, /:")

if z == "+":
    print("El resultado de la suma es: " + str(x + y))

elif z == "-":
    print("El resultado de la resta es: " + str(x - y))

elif z == "*":
    print("El resultado de la multiplicación es: " + str(x * y))

elif z == "/":
    print("El resultado de la división es: " + str(x / y))


