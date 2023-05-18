import json
from datetime import date
import os

def reemplazar_enies(palabra):
    if type(palabra) == str:
        nueva = palabra.replace("ñ","ni/")
        return nueva
    elif type(palabra) == list:
        for i in range(len(palabra)):
            palabra[i] = palabra[i].replace('ñ',"ni/")
        return palabra
 
def color_enies(palabra):
    nueva = palabra.replace("ni/","ñ")
    return nueva

#Instanciamos la clase animales que luego heredaremos a cada tipo de animal
class Animales:
    def __init__(self,nombre,edad,tamaño,dieta,especie,comidas,dormir,jugar,imagen):
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

        nombre_archivo = imagen.name
        """
        ruta_guardado = os.path.join(os.getcwd()+'images/', nombre_archivo)
        with open(ruta_guardado, "wb") as archivo:
            archivo.write(imagen.getbuffer())
        if os.path.exists(ruta_guardado):
            self.Imagen = ruta_guardado
        else:
            self.Imagen = os.path.join(os.getcwd()+'/ZOO/images/', 'imagen_generica.png')"""
        
        self.Imagen = " "
        

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
        dia_actual = date.today() #Tomamos el dia actual para saber si ya paso un dia y comparar el tiempo dormido
        permiso = True
        if dia_actual == self.dia:
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas: #Comparamos el tiempo dormido en el dia y el ingresado por el usuario
                permiso = False
        else:
            self.dia = dia_actual #Actualizamos el dia actual
            self.horas_sueño_tomadas = 0 #Reiniciamos el valor
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas: #Si la cantidad de horas supera las permitidas se niega el permiso
                permiso = False

        if permiso == True:
            self.horas_sueño_tomadas+=horas #Si el permiso es concedido, se suma las horas que se duerme 
            return (True,f'{self.nombre} esta durmiendo') #Se devuelve un mensaje y una confirmacion
        else:
            return (False, f'{self.nombre} no tiene permitido esa cantidad de horas de sueño') 
            #Si no se permite la accion, se envia un mensaje de negacion
        
    def jugar(self):
        dia_actual = date.today() #Comprobamos el dia actual para comparar con el almacenadao
        permiso = True
        if dia_actual == self.dia:
            if self.veces_jugadas == self.veces_jugar: #Si se alcanzaron las veces para jugar por dia se niega la accion
                permiso = False
        else:
            self.dia = dia_actual #Se actualiza el dia
            self.veces_jugadas = 0 #Se reinicia el contador
        
        if permiso:
            return (True, f'{self.nombre} esta jugando')
        else:
            return (False,f'{self.nombre} no puedes jugar mas por hoy')
        
    def guardar_info(self,datos=None):
        try:    
            with open('info.json','r',encoding='utf-8') as f:
                data = json.loads(f.read())
        except:
            with open('python\ZOO\info.json','r', encoding='utf-8') as f: 
                data = json.loads(f.read())
        
        if datos == None:
            nuevo_animal = {
                "Nombre":reemplazar_enies(self.nombre),
                "Edad":self.edad,
                "Tamanio":reemplazar_enies(self.tamaño),
                "Dieta":(self.dieta),
                "Temperatura":reemplazar_enies(self.temperatura),
                "Salud":reemplazar_enies(self.salud),
                "Tipo":reemplazar_enies(self.tipo),
                "Especie":reemplazar_enies(self.especie),
                "comidas_permitidas": (self.comidas_permitidas),
                "comidas_ingeridas":(self.comidas_ingeridas),
                "veces_jugar":(self.veces_jugar),
                "veces_jugadas":(self.veces_jugadas),
                "horas_suenio_permitidas":(self.horas_sueño_permitidas),
                "horas_suenio_tomadas":(self.horas_sueño_tomadas),
                "Habitat":reemplazar_enies(self.habitat),
                "Imagen":self.Imagen
            } 
        else:
            nuevo_animal = datos

        data['Animales'].append(nuevo_animal)

        try:
            with open('python\ZOO\info.json','w') as f:
                f.write(json.dumps(data,ensure_ascii=False))
        except:
            with open('info.json','w') as f:    
                f.write(json.dumps(data,ensure_ascii=False))

class Insectos(Animales): #Clase insectos, heredada de Animales
    def __init__(self, nombre, edad, tamaño, dieta, comidas,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos', comidas, -1, -1,imagen)  #Se definen parametros como constantes propias de los insectos
        self.tipo = 'Invertebrados'                                                #Los insectos no juegan, ni duermen
        self.temperatura = temperatura                                             #Y son invertebrados
        self.salud = salud                                                         #Se inicializan las variables del objeto
        self.habitat = habitat

    def dormir(self, horas=0): #Se sobreescribe y sobrecarga el metodo dormir, ya que los insectos tienen estado de reposo
        return f'El/la {self.nombre} es un insecto, estos animales aunque entran en estado de reposo no tienen tiempo estimado para dormir'
    
    def jugar(self): #Se sobrescribe el metodo jugar, ya que los insectos no tienen esa capacidad
        return f'El/la {self.nombre} es un insecto, son animales sin la capacidad de jugar'
    
class Mamiferos(Animales): #Clase mamiferos, heredada de Animales
    def __init__(self, nombre, edad, tamaño, dieta, comidas,dormir,jugar,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Mamiferos', comidas,dormir,jugar,imagen)  #Se usa el constructor de la clase padre
        self.tipo = 'Vertebrados'
        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat #Esta clase no sobreescribe los metodos de la padre ya que los mamiferos realizan las 3 acciones

class Aves(Animales): #Clase aves, herenciado de Animales
    def __init__(self, nombre, edad, tamaño, dieta, comidas,dormir,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos', comidas, dormir, -1,imagen)  
        self.tipo = 'Vertebrados'
        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat

    def jugar(self): #Se sobre escribe el metodo jugar de la clase aves, dependiendo de su tamaño
        if self.tamaño == 'pequeño':
            return f'El/la {self.nombre} le tiraste semillas, y vino revoloteando' 
        else:
            return f'El/la {self.nombre} es una especie demasiado grande para jugar'
    
class Peces(Animales): #Clase Peces, heredado de animales
    def __init__(self, nombre, edad, tamaño, dieta,vertebrado ,comidas,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos',comidas, -1, -1,imagen)  
        if vertebrado:    #En la categoria de peces existen vertebrados e invertebrados, asi que se agrega un capo al constructor
            self.tipo = 'Vertebrados'
        else: 
            self.tipo = 'Invertebrados' 

        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat

    def dormir(self, horas=0): #Se sobre escribe el metodo dormir
        return f'El/la {self.nombre} es un pez, estos animales aunque entran en estado de reposo no tienen tiempo estimado para dormir'
    
    def jugar(self): #Se sobreescribe el metodo jugar
        return f'El/la {self.nombre} es un pez, son animales sin la capacidad de jugar'

class Anfibios(Animales): #Clase Anfibios, heredado de animales
    def __init__(self, nombre, edad, tamaño, dieta, comidas,dormir,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos', comidas,dormir, -1,imagen)  
        self.tipo = 'Vertebrados'
        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat

    def jugar(self): #Se sobreescribe el metodo jugar 
        return f'El/la {self.nombre} esta dandose un chapuzon, super divertido!!!   '

class Reptiles(Animales):
    def __init__(self, nombre, edad, tamaño, dieta, comidas,dormir,temperatura,salud,habitat,imagen):
        super().__init__(nombre, edad, tamaño, dieta,'Insectos', comidas, dormir, -1, imagen)  
        self.tipo = 'Vertebrados'
        self.temperatura = temperatura
        self.salud = salud
        self.habitat = habitat

    def jugar(self): #Se sobre escribe el metodo jugar
        return f'El/la {self.nombre} esta tomando el sol, esta bastante relajado'

class Comida:
    def __init__(self, nombre, dietas, tamaño):
        self.nombre = nombre
        self.dietas = dietas
        self.tamaño = tamaño

class Habitat():
    def __init__(self,nombre,tipo,espacio_dispoible,temperatura,dieta,tipo_animal,especies):
        self.nombre = nombre
        self.tipo = tipo
        self.espacio_disponible = espacio_dispoible
        self.espacio_ocupado = 0
        self.temperatura = temperatura
        self.dieta = dieta
        self.tipo_animal = tipo_animal
        self.especies = especies
        self.animales = []

    def agregar_animal(self,animal):
        pass
        #if animal.


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

class image():
    def __init__(self,nombre):
        self.name = nombre


imagen = image('hormiga.png')

insecto_nuevo = Insectos('Hormiga',0.16,'pequeño','Omnivora',8,['Tropical','Templado','Calido'],'Saludable','Sabana',imagen=imagen)
comida_nueva = Comida('Semillas',['Omnivora','Hervivoros'],'pequeño')
#print(insecto_nuevo.jugar())
#print(insecto_nuevo.dormir())
#print(insecto_nuevo.comer(comida=comida_nueva)[1])
insecto_nuevo.guardar_info()



with open('info.json','r') as f: 
    data = json.loads(f.read())

print(data['Animales'][2])