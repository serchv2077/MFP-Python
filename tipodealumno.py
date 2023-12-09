#Preguta calificacion.
cal = float(input("Cual es tu calificacion: "))
#clasificar por calificacion
if cal == 100:
    print("Excelente")
elif 90 <= cal <= 99:
    print("Muy bueno")
elif 80 <= cal <= 89:
    print("Bueno")
elif 70 <= cal <= 79:
    print("Regular")
elif 60 <= cal <= 69:
    print("Malo")
else:
    print("Reprobado")