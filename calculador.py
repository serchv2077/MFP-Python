#Importamos libreria math para factorial
from math import factorial

# Bucle hasta que sea 6
while True:
    #Sentencia para validar la entrada
    try:
        #Menu
        seleccion = int(input("Que quieres calcular? 1.- Suma 2.- Resta 3.- Multiplicacion 4.- division 5.-Factorial 6.-Exit: "))
        #Selecciones
        if seleccion == 6: 
            break
        a=float(input("Dame tu primer numero: "))
        b=float(input("Dame tu segundo numero: "))

        if(seleccion == 1):
            print("Tu suma es: ", a+b)
       
        elif(seleccion == 2):
            print("Tu resta es: ", a-b)
          
        elif(seleccion == 3):
            print("Tu multiplicacion es: ", a*b)
        
        elif(seleccion == 4):
            print("Tu Division  es: ", a/b)
        elif(seleccion == 5):
        
            fact=int(input("Que numero quieres fatorial: "))
            print("Tu factorial es: ", factorial(fact))
            #Si no cumple ninguno.
        else:
            print("Opcion no valida, elije otra opcion: ")
            #Acompañamnientos del try de sentencias.
    except ValueError:
        print("La opción que ingresaste no es válida. Por favor, ingresa un número.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")

print("Gracias por usarme :)")