import random

def code():
    x = random.randint(1000, 9999)
    print("Tu codigo del gym ahora es: ", x)
    return x
def ver(codigo):
    while  True:
        ver = int(input("verficica tu codigo: "))
        if(ver==codigo):
            print("Welcome")
            break
        elif(codigo):
            print("Invalid")
est=int(input("Eres estudiante 1.-Si   2.-No: "))
if est==1:
    y=("$350")
elif est ==2:
    y=400
codigo=code()
print("Bienvenido usuario, tu codigo y cuota es: ", codigo, y)
ver(codigo)