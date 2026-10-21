import random

num_adivinar = random.randint(1, 10)

val = int(input("Introduce un número entre 1 y 10: "))
intentos = 3

if val == num_adivinar:
    print("¡Has adivinado!")
else:
    print(f"Te quedan {intentos - 0} intentos:")
    print(f"El número es mayor que {val}" if val < num_adivinar else f"El número es menor que {val}")
    val = int(input("Introduce un número entre 1 y 10: "))
   
if val == num_adivinar:
    print("¡Has adivinado!")
else:
    print(f"Te quedan {intentos - 1} intentos:")
    print(f"El número es mayor que {val}" if val < num_adivinar else f"El número es menor que {val}")
    val = int(input("Introduce un número entre 1 y 10: "))

if val == num_adivinar:
    print("¡Has adivinado!")
else:
    print(f"El número es mayor que {val}" if val < num_adivinar else f"El número es menor que {val}")
    print(f"Te quedan {intentos - 2} intentos:")
    val = int(input("Introduce un número entre 1 y 10: "))

    print(f"El número correcto era: {num_adivinar}")