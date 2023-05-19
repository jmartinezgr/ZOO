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
 
def poner_enies(palabra):
    if type(palabra) == str:
        nueva = palabra.replace("ni/","ñ")
        return nueva
    elif type(palabra) == list:
        for i in range(len(palabra)):
            palabra[i] = palabra[i].replace('ni/',"ñ")
        return palabra

#Instanciamos la clase animales que luego heredaremos a cada tipo de animal
class Animales:
    def __init__(self,dic=None,nombre=None,edad=None,tamaño=None,dieta=None,especie=None,comidas=None,dormir=None,jugar=None):
        if dic== None:
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
            self.dia = date.today().isoformat() #Se almacenara en primera instancia el dia que se crea el animal

            #nombre_archivo = imagen.name
            """
            ruta_guardado = os.path.join(os.getcwd()+'images/', nombre_archivo)
            with open(ruta_guardado, "wb") as archivo:
                archivo.write(imagen.getbuffer())
            if os.path.exists(ruta_guardado):
                self.Imagen = ruta_guardado
            else:
                self.Imagen = os.path.join(os.getcwd()+'/ZOO/images/', 'imagen_generica.png')"""
            
            #self.Imagen = " "
        else:
            self.nombre = dic['Nombre']
            self.edad = dic['Edad']
            self.tamaño = dic['Tamanio']
            self.dieta = dic['Dieta']
            self.especie = dic['Especie']
            self.comidas_permitidas = dic['comidas_permitidas']
            self.comidas_ingeridas = dic['comidas_ingeridas']
            self.horas_sueño_permitidas = dic['horas_suenio_permitidas']
            self.horas_sueño_tomadas = dic['horas_suenio_tomadas']
            self.veces_jugar = dic['veces_jugar']
            self.veces_jugadas = dic['veces_jugadas']
            self.dia = dic['Dia']

    def comer(self,comida):
        dia_actual = date.today().isoformat() #Tomamos el dia actual para saber si ya paso un dia y comparar las comidas diarias
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
        
    def dormir(self,horas=1):
        dia_actual = date.today().isoformat() #Tomamos el dia actual para saber si ya paso un dia y comparar el tiempo dormido
        permiso = True
        print(self.horas_sueño_tomadas)
        if dia_actual == self.dia:
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas: #Comparamos el tiempo dormido en el dia y el ingresado por el usuario
                permiso = False
        else:
            self.dia = dia_actual #Actualizamos el dia actual
            self.horas_sueño_tomadas = 0 #Reiniciamos el valor
            if (self.horas_sueño_permitidas-self.horas_sueño_tomadas) < horas: #Si la cantidad de horas supera las permitidas se niega el permiso
                permiso = False

        if permiso == True:
            print(self.horas_sueño_tomadas)
            self.horas_sueño_tomadas += horas #Si el permiso es concedido, se suma las horas que se duerme 
            print(self.horas_sueño_tomadas)
            return (True,f'{self.nombre} esta durmiendo') #Se devuelve un mensaje y una confirmacion
        else:
            return (False, f'{self.nombre} no tiene permitido esa cantidad de horas de sueño') 
            #Si no se permite la accion, se envia un mensaje de negacion
        
    def jugar(self):
        dia_actual = date.today().isoformat() #Comprobamos el dia actual para comparar con el almacenadao
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
        
    def guardar_info(self,datos=None,tipo='c'):
        try:    
            with open('info.json','r') as f:
                data = json.loads(f.read())
        except:
            with open('python\ZOO\info.json','r') as f: 
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
                "horas_suenio_tomadas":self.horas_sueño_tomadas,
                "Habitat":reemplazar_enies(self.habitat),
                "Dia":self.dia
            } 
        else:
            nuevo_animal = datos

        if tipo == 'c':
            data['Animales'].append(nuevo_animal)
        else:
            for i in range(len(data['Animales'])):
                if data['Animales'][i]['Nombre'] == nuevo_animal['Nombre']:
                    data['Animales'][i] = nuevo_animal
                    

        
        with open('info.json','w') as f:    
            f.write(json.dumps(data))

class Insectos(Animales): #Clase insectos, heredada de Animales
    def __init__(self,dic=None, nombre=None, edad=None, tamaño=None, dieta=None, comidas=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta,especie='Insectos', comidas=comidas, dormir=-1,jugar= -1)  #Se definen parametros como constantes propias de los insectos
        if dic ==None:
            self.tipo = 'Invertebrados'                                                #Los insectos no juegan, ni duermen
            self.temperatura = temperatura                                             #Y son invertebrados
            self.salud = salud                                                         #Se inicializan las variables del objeto
            self.habitat = habitat
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

    def dormir(self, horas=0): #Se sobreescribe y sobrecarga el metodo dormir, ya que los insectos tienen estado de reposo
        return f'El/la {self.nombre} es un insecto, estos animales aunque entran en estado de reposo no tienen tiempo estimado para dormir'
    
    def jugar(self): #Se sobrescribe el metodo jugar, ya que los insectos no tienen esa capacidad
        return f'El/la {self.nombre} es un insecto, son animales sin la capacidad de jugar'
    
class Mamiferos(Animales): #Clase mamiferos, heredada de Animales
    def __init__(self,dic=None,nombre=None, edad=None, tamaño=None, dieta=None, comidas=None,dormir=None,jugar=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta, especie='Mamiferos', comidas=comidas,dormir=dormir,jugar=jugar)  #Se usa el constructor de la clase padre
        if dic == None:
            self.tipo = 'Vertebrados'
            self.temperatura = temperatura
            self.salud = salud
            self.habitat = habitat #Esta clase no sobreescribe los metodos de la padre ya que los mamiferos realizan las 3 acciones
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

class Aves(Animales): #Clase aves, herenciado de Animales
    def __init__(self,dic=None, nombre=None, edad=None, tamaño=None, dieta=None, comidas=None,dormir=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta,especie='Aves', comidas=comidas, dormir=dormir, jugar=-1)  
        if dic == None:
            self.tipo = 'Vertebrados'
            self.temperatura = temperatura
            self.salud = salud
            self.habitat = habitat
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

    def jugar(self): #Se sobre escribe el metodo jugar de la clase aves, dependiendo de su tamaño
        if self.tamaño == 'pequeño':
            return f'El/la {self.nombre} le tiraste semillas, y vino revoloteando' 
        else:
            return f'El/la {self.nombre} es una especie demasiado grande para jugar'
    
class Peces(Animales): #Clase Peces, heredado de animales
    def __init__(self,dic = None, nombre=None, edad=None, tamaño=None, dieta=None,vertebrado = None ,comidas=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta,especie='Peces',comidas=comidas,dormir=-1, jugar=-1)  
        if dic == None:
            if vertebrado:    #En la categoria de peces existen vertebrados e invertebrados, asi que se agrega un capo al constructor
                self.tipo = 'Vertebrados'
            else: 
                self.tipo = 'Invertebrados' 

            self.temperatura = temperatura
            self.salud = salud
            self.habitat = habitat
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

    def dormir(self, horas=0): #Se sobre escribe el metodo dormir
        return f'El/la {self.nombre} es un pez, estos animales aunque entran en estado de reposo no tienen tiempo estimado para dormir'
    
    def jugar(self): #Se sobreescribe el metodo jugar
        return f'El/la {self.nombre} es un pez, son animales sin la capacidad de jugar'

class Anfibios(Animales): #Clase Anfibios, heredado de animales
    def __init__(self,dic=None, nombre=None, edad=None, tamaño=None, dieta=None, comidas=None,dormir=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta,especie='Anfibios', comidas=comidas,dormir=dormir,jugar= -1)  
        if dic == None:
            self.tipo = 'Vertebrados'
            self.temperatura = temperatura
            self.salud = salud
            self.habitat = habitat
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

    def jugar(self): #Se sobreescribe el metodo jugar 
        return f'El/la {self.nombre} esta dandose un chapuzon, super divertido!!!   '

class Reptiles(Animales):
    def __init__(self,dic=None,nombre=None, edad=None, tamaño=None, dieta=None, comidas=None,dormir=None,temperatura=None,salud=None,habitat=None):
        super().__init__(dic=dic,nombre=nombre, edad=edad, tamaño=tamaño, dieta=dieta,especie='Insectos', comidas=comidas, dormir=dormir, jugar=-1)  
        if dic == None:
            self.tipo = 'Vertebrados'
            self.temperatura = temperatura
            self.salud = salud
            self.habitat = habitat
        else:
            self.tipo = dic['Tipo']
            self.temperatura = dic['Temperatura']
            self.salud = dic['Salud']
            self.habitat = dic['Habitat']

    def jugar(self): #Se sobre escribe el metodo jugar
        return f'El/la {self.nombre} esta tomando el sol, esta bastante relajado'

class Comida:
    def __init__(self, nombre, dietas, tamaño):
        self.nombre = nombre
        self.dietas = dietas
        self.tamaño = tamaño

    def cargar_info(self):
        try:    
            with open('info.json','r',encoding='utf-8') as f:
                data = json.loads(f.read())
        except:
            with open('python\ZOO\info.json','r', encoding='utf-8') as f: 
                data = json.loads(f.read())

        info = {
            "Nombre":reemplazar_enies(self.nombre),
            "Dietas":reemplazar_enies(self.dietas),
            "Tamanio": reemplazar_enies(self.tamaño)
        }

        data['Comidas'].append(info)

        try:
            with open('python\ZOO\info.json','w') as f:
                f.write(json.dumps(data,ensure_ascii=False))
        except:
            with open('info.json','w') as f:    
                f.write(json.dumps(data,ensure_ascii=False))
        

class Habitat():
    def __init__(self,dic=None,nombre=None,tipo=None,espacio_dispoible=None,temperatura=None,dieta=None,tipo_animal=None,especies=None,animales=None):
        if dic==None:
            self.nombre = nombre
            self.tipo = tipo
            self.espacio_disponible = espacio_dispoible
            self.espacio_ocupado = 0
            self.temperatura = temperatura
            self.dieta = dieta
            self.tipo_animal = tipo_animal
            self.especies = especies
            self.animales = animales
        else:
            self.nombre = poner_enies(dic['Nombre'])
            self.tipo = poner_enies(dic['Tipo'])
            self.espacio_disponible = dic['Espacio_disponible']
            self.espacio_ocupado = dic['Espacios_ocupados']
            self.temperatura = poner_enies(dic['Temperatura'])
            self.dieta = poner_enies(dic['Dieta'])
            self.tipo_animal = poner_enies(dic['Tipo_animal'])
            self.especies = poner_enies(dic['Especies'])
            self.animales = poner_enies(dic['Nombre_animales'])

    def agregar_animal(self,nombre,tamaño,dieta,especie):
        permiso = True
        espacio = self.espacio_disponible-self.espacio_ocupado
        if tamaño == 'pequeño':
            espacio_animal = 1
        elif tamaño =='mediano':
            espacio_animal = 2
        elif tamaño == 'grande':
            espacio = 3
        
        if espacio < espacio_animal:
            permiso = False

        if not dieta in self.dieta:
            permiso = False
        
        if not especie in self.especies:
            permiso = False

        if permiso:
            self.animales.append(nombre)
            return True
        else:
            return False
        
    def cargar_habitat(self):
        try:    
            with open('info.json','r') as f:
                data = json.loads(f.read())
        except:
            with open('python\ZOO\info.json','r') as f: 
                data = json.loads(f.read())
        
        info = {
            "Nombre": reemplazar_enies(self.nombre),
            "Tipo":reemplazar_enies(self.tipo),
            "Espacio_disponible": self.espacio_disponible,
            "Espacios_ocupados": self.espacio_ocupado,
            "Temperatura": reemplazar_enies(self.temperatura),
            "Dieta": reemplazar_enies(self.dieta),
            "Tipo_animal": reemplazar_enies(self.tipo_animal),
            "Especies": reemplazar_enies(self.especies),
            "Nombre_animales": reemplazar_enies(self.animales)
        }

        data['Habitats'].append(info)

        with open('info.json','w') as f:    
                f.write(json.dumps(data))

class Zoologico:
    def __init__(self):
        self.tipos_habitats = ["Selvatico","Desertico","Polar","Acuatico"]
        self.tipos_animales = ["Mamiferos","Invertebrados","Peces","Anfibios","Reptiles","Aves"]
        self.habitats = []
        self.animales = []
        self.comidas = []

    def cargarInfo(self):
        with open('info.json','r') as f:
            data = json.loads(f.read())

        for habitat in data['Habitats']:
            self.habitats.append(habitat['Nombre'])
        
        for animal in data['Animales']:
            self.animales.append(animal['Nombre'])
        
        for comida in data['Comidas']:
            self.comidas.append(comida['Nombre'])
        
    def get_animales(self):
        return self.animales

    def get_habitats(self):
        return self.habitats
    
    def get_comidas(self):
        return self.comidas
    
    def get_tipos_habitats(self):
        return self.tipos_habitats

    def get_tipos_animales(self):
        return self.tipos_animales



"""

imagen = image('hormiga.png')

insecto_nuevo = Insectos(None,'Hormiga',0.16,'pequeño','Omnivora',8,['Tropical','Templado','Calido'],'Saludable','Sabana')
comida_nueva = Comida('Semillas',['Omnivora','Hervivoros'],'pequeño')
#print(insecto_nuevo.jugar())
#print(insecto_nuevo.dormir())
#print(insecto_nuevo.comer(comida=comida_nueva)[1])
insecto_nuevo.guardar_info()


with open('info.json','r') as f: 
    data = json.loads(f.read())

print(data['Animales'][2])

"""  
