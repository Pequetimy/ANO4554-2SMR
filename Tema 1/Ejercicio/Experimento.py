número = int(input("Introduce un número del 1 al 10:"))
if número > 10 :
    input("error: Introduce un número del 1 al 10:")

for x in range(1, 1001):
    tabla = número * x
    print(f"La tabla de {número} x {x} = {tabla}")