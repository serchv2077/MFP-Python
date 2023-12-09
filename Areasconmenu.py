#Imprimimos un menu
seleccion = int(input("De qué quieres calcular el área? 1.- Triángulo 2.- Círculo 3.- Cuadrado 4.- Salir: "))
#Bucle para que  pregunte varias veces hasta que presione 4
while seleccion != 4:
    if (seleccion == 1):
        base = int(input("Cuál es tu base: "))
        altura = int(input("Cuál es tu altura: "))
        area = base * altura / 2
        print("Tu área del triángulo es: ", area)
    elif (seleccion == 2):
        radio = int(input("Cuál es el radio: "))
        area = 3.14159 * radio * radio
        print("Tu área del círculo es: ", area)
    elif (seleccion == 3):
        lado = int(input("Cuál es el lado de tu cuadrado: "))
        area = lado * lado
        print("Tu área es: ", area)
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
#Para que vuelva a imprimir.
    seleccion = int(input("De qué quieres calcular el área? 1.- Triángulo 2.- Círculo 3.- Cuadrado 4.- Salir: "))

print("Adiós. Gracias por usar el programa.")
