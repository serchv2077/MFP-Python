#pregutar  un caracter
caracter=ord(input("Ingresa un caracter"))
#seperar por codigo ascii
if( 65 <=caracter <= 90):
    print("Tu caracter es mayuscula", chr(caracter))
elif(97 <= caracter <= 122):
    print("Tu caracter es minusculo", chr(caracter))
elif(48 <= caracter <= 57):
    print("Tu Caracter es un digito", chr(caracter))
else:
    print("Tu caracter es especial", chr(caracter))