opcion=int(input("¿De que quieres hacer convesion 1.-Dolar a peso  2.-Peso a dolar")) #Preguntar una opcion tipo menu
if(opcion==1):                                                                        #Si es uno hacer esto
    dolar=float(input("Cuantos dolares quieres convertir?"))
    print("Tu consersion es: ", dolar*17.60)                        #Resultado
elif(opcion==2):                                                                         #Si es dos hacer esto
    peso=float(input("Cuantos pesos quieres convertir?"))
    print("Tu conversion es: ", peso/17.60)                              #Resultado