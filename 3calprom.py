l=float(input("Cual es tu calificacion de logica"))
m=float(input("Cual es tu calificacion de matematicas"))             #Pregunto la caplificacion de las tres materias
f=float(input("Cual es tu calificacion de fisica"))

prom=(l+m+f)/3      #Operacion de promedio

if(prom>=95):            #Paramatros para imprimir 100
    print("Tu calificacion es de 100")
else:                 #Si no cumple paramatros.
    print("Deberes mejorar el promedio para participar", prom)