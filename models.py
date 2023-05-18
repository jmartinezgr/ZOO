import json
from datetime import date
#Instanciamos la clase animales que luego heredaremos a cada tipo de animal
class Animales:
    def __init__(self,nombre,edad,tamaño,dieta,especie,comidas,dormir,jugar):
        self.nombre = nombre
        self.edad = edad
        self.tamaño = tamaño
        self.dieta = dieta
        self.especie = especie
        self.comidas_permitidas = comidas
        self.comidas_ingeridas = 0
        self.horas_sueño_permitidas = dormir
        self.horas_sueño_tomadas = 0
        self.veces_jugar = jugar
        self.veces_jugadas = 0
        self.dia = date.today() #Se almacenara en primera instancia el dia que se crea el animal

    def comer(self,comida):
        dia_actual = date.today() #Tomamos el dia actual para saber si ya paso un dia y comparar las comidas diarias
        permiso = True
        if self.dia == dia_actual:
            if self.comidas_ingeridas == self.comidas_permitidas:
                permiso = False #Si es el mismo dia almacenado en el objeto y ya se le dieron las comidas permitas
        else:                   #Es denegada la accion de comer para este animal
            self.dia = dia_actual  
            self.comidas_ingeridas = 0  #Si el dia paso, se cambia la fecha almacenada y se reinicia el contador
            
        if permiso:                     #Si no hay razones para cancelar el permiso
            for tipo in comida.dietas:    
                #Si itera los tipos de alimetacion que tiene el alimento y se comprueba si el animal lo recibe
                if tipo in self.dieta and self.tamaño == comida.tamaño:
                    self.comidas_ingeridas += 1  #Si se comprueba la compatibilidad se agrega una comida en el dia
                    return (True,f'{self.nombre} esta comiendo {comida.nombre}') #Se devuelve el mensaje que se va a imprimir por pantalla
            #Si el tipo no es compatible, se retorna un mensaje de negacion
            return (False, f'{comida.nombre} no esta permitido en la dieta de {self.nombre}')
        else:
            #Si el animal ha comido suficientes veces
            return (False,f'{self.nombre} ya comio suficiente hoy')
        
    def dormir(self,horas):
        dia_actual = date.today() #Tomamos el dia actual para saber si ya paso un dia y comparar las comidas diarias
        permiso = True
        if dia_actual == self.dia:
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas:
                permiso = False
        else:
            self.dia = dia_actual
            self.horas_sueño_tomadas = 0
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas:
                permiso = False

        if permiso == True:
            self.horas_sueño_tomadas+=horas 
            return (True,f'{self.nombre} esta durmiendo')
        else:
            return (False, f'{self.nombre} no tiene permitido esa cantidad de horas de sueño')
        
    def jugar(self):
        dia_actual = date.today()
        permiso = True
        if dia_actual == self.dia:
            if self.veces_jugadas == self.veces_jugar:
                permiso = False
        else:
            self.dia = dia_actual
            self.veces_jugadas = 0
        
        if permiso:
            return (True, f'{self.nombre} esta jugando')
        else:
            return (False,f'{self.nombre} no puedes jugar mas por hoy')

class Insectos(Animales):
    def __init__(self, nombre, edad, tamaño, dieta, comidas,temperatura,salud,habitat):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos', comidas, -1, -1)  
        self.tipo = 'Invertebrados'
        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat

    def dormir(self, horas=0):
        return f'El/la {self.nombre} es un insecto, estos animales aunque entran en estado de reposo no tienen tiempo estimado para dormir'
    
    def jugar(self):
        return f'El/la {self.nombre} es un insecto, son animales sin la capacidad de jugar'

class Comida:
    def __init__(self, nombre, dietas, tamaño):
        self.nombre = nombre
        self.dietas = dietas
        self.tamaño = tamaño

class Zoologico:
    def __init__(self):
        self._tipos_habitats = ["Selvatico","Desertico","Polar","Acuatico"]
        self._tipos_animales = ["Mamiferos","Invertebrados","Peces","Anfibios","Reptiles","Aves"]
        self.habitats = []
        self.animales = []
        self.comidas = []

    def cargarInfo(self):
        with open('info.json','r') as f:
            data = json.loads(f.read())
    
    def agregar_animal(self):
        pass

    def agregar_habitat(self):
        pass

    def mostrar_animales(self):
        pass

    def mostrar_habitats(self):
        pass

"""
insecto_nuevo = Insectos('Hormiga',0.16,'pequeño','Omnivora',8,['Tropial','Templado','Calido'],'Saludable','Sabana')
comida_nueva = Comida('Semillas',['Omnivora','Hervivoros'],'pequeño')
print(insecto_nuevo.jugar())
print(insecto_nuevo.dormir())
print(insecto_nuevo.comer(comida=comida_nueva)[1])"""