import models
import json
import requests
import subprocess

def buscar_animal(nombre):
    with open('info.json','r') as f:
        data = json.loads(f.read())


    for animal in data['Animales']:
    
        if animal['Nombre'] == nombre:
         
            if animal['Especie'] == 'Mamiferos':
                nuevo_animal = models.Mamiferos(dic=animal)
            elif animal['Especie'] == 'Insectos':
                nuevo_animal = models.Insectos(dic=animal)
            elif animal['Especie'] == 'Reptiles':
                nuevo_animal = models.Reptiles(dic=animal)
            elif animal['Especie'] == 'Aves':
                nuevo_animal = models.Aves(dic=animal)
            elif animal['Especie'] == 'Peces':
                nuevo_animal = models.Peces(dic=animal)
            elif animal['Especie'] == 'Anfibios':
                nuevo_animal = models.Anfibios(dic=animal)
            
            return nuevo_animal

def buscar_habitat(nombre):
    with open('info.json','r') as f:
        data = json.loads(f.read())

    for habitat in data['Habitats']:
        if habitat['Nombre'] == nombre:
            
            habitat_encontrado = models.Habitat(dic=habitat)
            
            return habitat_encontrado