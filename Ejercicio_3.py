nombre = input("\n¿Cual es tu nombre?  ")
numero = int(input("¿Que número elegiste?  "))

print("")
if numero < 1: print("Error 42. Tienes que elegir un número mayor que 0")
else: 
    for i in range(numero):
        print(nombre, end = " ")
print("")