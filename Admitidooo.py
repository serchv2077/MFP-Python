cal1=float(input("¿Cual es tu calificacion del certificado?"))
cal2=float(input("¿Cual es tu calificacion del examen?"))
tot=(cal1 + cal2)/2
if(tot>=85):
        print("fuiste admitido: ", tot)
else:
    print("No fuiste admitido", tot)
