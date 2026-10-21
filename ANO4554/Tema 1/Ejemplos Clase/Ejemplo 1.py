nombre = input("Introducir tu nombre: ")
edad = input("Introducir tu edad: ")
año = 2026 - int(edad)
mes = int(edad) * 12
print( "Hola " + nombre + " tiene " + str(mes) + " meses" + " y naciste en el año " + str(año))
print(f"Tu nombre es {nombre} y tu edad es {edad} años, naciste en el año {año} y tienes {mes} meses") 
if int(año) > 2010:
    print("Eres Cristalito")
if int(edad) >= 18: 
    print("Eres mayor de edad")

