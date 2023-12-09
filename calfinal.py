l=float(input("Cual es tu calificacion de logica"))
m=float(input("Cual es tu calificacion de matematicas"))
f=float(input("Cual es tu calificacion de fisica"))

prom=(l+m+f)/3

if(prom>79):
    print("Eres acreditador a una beca con un promedio de:  ", prom)
else:
    print("Deberes mejorar el promedio para participar", prom)