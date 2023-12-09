#caracterisitcas preguntadas
p=int(input("A cuanto te pagan la hora"))
z=int(input("Cuantas horas trabajaste"))
q=int(input("Cuantas horas extras trabajaste"))
sal=p*40
#condicion de pago extra
if(z>40):
    print("Tu salario es de: ", sal+(q*1.5))  
#pago normal
else:
    print("Tu salario es: ", sal)