nota = float(input("Que nota númerica sacaste?  "))

if nota < 0 or nota > 10: 
    print("Creo que te equivocaste al introducir la nota, recuerda que tiene que estar entre 0  y 10")
    
else:
    print("Eso corresponde a un", end = " ")
    if nota < 5: print("Suspenso. Deberías estudiar más!!!")
    elif nota < 7: print("Aprobado. De buena te has librado!!!")
    elif nota < 9: print("Notable. Buen trabajo!!!")
    else: print("Excelente. FELICIDADES!!!")