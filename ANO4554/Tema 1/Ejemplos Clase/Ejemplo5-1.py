#Ejemplo5-1.py
edad = int(input("Pon tu edad:"))
altura = int(input("Pon tu altura:"))
if (edad >= 18 and altura >=180):
    print("Estas calificados para las pruebas")

elif (edad < 18):
    print("Eres menor de edad")

elif (altura < 180):
    print("No tienes la altura requerida")

elif (altura < 180 and edad < 18):
    print("No cumples con la edad ni con la altura requerida")

else:
    print("No cumple las condiciones para poder haceder a las pruebas")

print("Fin")