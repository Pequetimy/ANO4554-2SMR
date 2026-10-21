import random
num_adivinar = random.randint(1, 100)
intentos = 0

while(intentos < 5):
    val = int(input("Introduce un número entre 1 y 100: "))
    intentos = intentos+1
    
    if num_adivinar == val:
        print(f"¡Has ganado, el número era! {num_adivinar}")
        break
    
    elif num_adivinar < val:
        print(f"El número es menor que {val}")
        print(f"Te quedan {intentos} intentos:")

    elif num_adivinar > val:
        print(f"El número es mayor que {val}")
        print(f"Te quedan {intentos} intentos:")
else:
    print(f"¡Has perdido, el número era! {num_adivinar}")