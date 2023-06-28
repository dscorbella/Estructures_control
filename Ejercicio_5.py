rango_lista = int(input("\nCuantos valores va a tener la lista?  "))

lista = []
print("")
for n in range(rango_lista):
    lista.append(int(input("Cual será el siguiente valor?  " )))

coincidencia = []
if len(lista) == 0: print("\nEsta lista está vacía.")
else:
    for i in range(len(lista)):    
        if i == lista[i]: coincidencia.append(i)
    
    if len(coincidencia) == 0: print("\nNo hay coincidencias.")
    elif len(coincidencia) ==1: print("\nSolo coincide el", coincidencia[0])
    else:
        print("\nLos números que coinciden son:", end = " ")
        for k in range(len(coincidencia)):
            print(coincidencia[k], end = "")
            if k + 2 < len(coincidencia): print(",", end = " ")
            elif k + 2 == len(coincidencia): print(" y", end = " ")
            else: print(".")