import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura tus credenciales de Gmail
tu_correo = ""
tu_contraseña = ""

# Lista de nombres y direcciones de correo electrónico
participantes = {
    "Christina": "papa@gmail.com",
    "sergio": "sergio.gutierrez1520@gmail.com",
    "boti": "correo3@gmail.com",
    # Agrega más personas según sea necesario
}

# Mezcla la lista de nombres para asignar "Amigos Secretos"
nombres = list(participantes.keys())
random.shuffle(nombres)

# Configura y envía los correos electrónicos
for i in range(len(nombres)):
    amigo_secreto = nombres[(i + 1) % len(nombres)]
    persona = nombres[i]
    correo_destino = participantes[persona]
    
    mensaje = MIMEMultipart()
    mensaje["From"] = tu_correo
    mensaje["To"] = correo_destino
    mensaje["Subject"] = "¡Tu Amigo Secreto para el intercambio de regalos!"
    
    cuerpo = f"Hola {persona},\n\nTu Amigo Secreto para el intercambio de regalos es: {amigo_secreto}.\n\n¡Felices fiestas!"
    mensaje.attach(MIMEText(cuerpo, "plain"))
    
    # Conéctate al servidor de Gmail y envía el correo
    try:
        servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_smtp.starttls()
        servidor_smtp.login(tu_correo, tu_contraseña)
        servidor_smtp.sendmail(tu_correo, correo_destino, mensaje.as_string())
        servidor_smtp.quit()
        print(f"Correo enviado a {persona} ({correo_destino})")
    except Exception as e:
        print(f"Error al enviar correo a {persona}: {str(e)}")
