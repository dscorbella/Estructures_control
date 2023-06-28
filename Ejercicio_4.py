tamaño_lista = int(input("\nCuantos valores va a tener la lista?  "))

lista = []
print("")
for n in range(tamaño_lista):
    lista.append(int(input("Cual será el siguiente valor?  " )))

if len(lista) == 0: print("\nEsta lista está vacía.")
elif tamaño_lista == 1: print("\nEsta lista es simetrica y tiene un único elemento")
else:
    for i in range((tamaño_lista)//2):
        if lista[i] != lista[tamaño_lista - 1 - i]:
            print("\nEsta lista no es simétrica.")
            break
    
    else: print("\nEsta lista es simétrica, y tiene", tamaño_lista, "elementos.")