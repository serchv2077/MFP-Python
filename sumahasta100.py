contador=0                                                              #Iniciamos nuestra suma en 0
while(contador<=100):                                                    #blucle hasta que sea 100
    i=int(input("Dame un numero para sumar"))                               #pregunta el numero 
    contador+=i                                                                  #suma 
if(contador>=100):                                                      # condicion para pararlo y no vuelva a preguntar
    print("Tu suma es", contador)                                           # resultado