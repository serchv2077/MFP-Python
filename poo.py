class personaje:                                      # Declarar la clase 
   
    def __init__(self,nombre,fuerza,defensa,vida,inteligencia):  # corresponden a los atributos de la clase 
        self.nombre=nombre
        self.fuerza=fuerza
        self.defensa=defensa
        self.vida=vida
        self.inteligencia=inteligencia
    
    def atributos(self):                                    # Bloque de atributos genereales
        print(self.nombre, ":", sep="")
        print("fueza", self.fuerza)
        print("Defensa", self.defensa)
        print("Vida", self.vida)
        print("inteligencia", self.inteligencia)
    
    def subir_nivel(self,fuerza,vida,inteligencia):             # Bloque para subir de nivel 
        self.fuerza=self.fuerza + fuerza
        self.vida=self.vida + vida
        self.inteligencia=self.inteligencia + inteligencia
     
    def esta_vivo(self):                                              #  Bloque para revisar si esta vivo si es mayor a 0 sera True , si no sera false.
        return self.vida > 0 
    
    def morir(self):                                                #Bloque para matara al personaje
        self.vida= 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):                                      # Bloque para calcular el daño
        return self.fuerza - enemigo.defensa
        
    def ataque(self, enemigo):
        daño=self.daño(mi_enemigo)
        mi_enemigo.vida= mi_enemigo.vida-daño
        print(self.nombre, "Ha realizado", daño, "Puntos de daño a ", mi_enemigo.nombre)
        if enemigo.esta_vivo():                                                            # Aplicamos nuestro bloque para revisar si ha mueto, si devuelve un true imprime normal 
            print("La vida de", mi_enemigo.nombre, "Es", mi_enemigo.vida)
        else:                                                                           
            enemigo.morir()                                                                 #Si devuelve un false , aplicamos el bloque de morir


mi_personaje=personaje("Artorias", 700, 40, 500, 100)                                #Iniciamos nuestro personaje 
mi_enemigo=personaje("Valdur", 600 ,78, 499, 50)
##mi_personaje.atributos()                                                            #imprimes el bloque de atributos 
##print(mi_personaje.esta_vivo())                                                   # Para saber si el personaje esta vivo
##mi_personaje.morir()                                                             # Matar al personaje y presentar mensaje
##print(mi_personaje.daño(mi_enemigo))
mi_personaje.ataque(mi_enemigo)
