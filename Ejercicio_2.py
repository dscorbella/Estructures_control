primero = int(input("\nCual será el primer número?  "))
segundo = int(input("Y ahora introduce el segundo:  "))

print("")

if primero > segundo: print(primero, "es mayor que", segundo)
elif primero < segundo: print(primero, "es menor que", segundo)
else: print("Son iguales.")