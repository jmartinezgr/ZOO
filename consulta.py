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
        
"""
def api(nombre):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(nombre)

    response = requests.get(api_url, headers={'X-Api-Key': 'evHip6n7q2JMBxeDTXU2xg==5x04BinR0gWXoU3A'})
    if response.status_code == requests.codes.ok:
        response_data = json.loads(response.text)
        #for i in response_data:
        caracteristicas = response_data[0]['characteristics']

        #clista = [['Esperanza de vida',caracteristicas['lifespan']],['Madurez Sexual',caracteristicas['age_of_sexual_maturity']]]
    else:
        print("Error:", response.status_code, response.text)
"""

#api('Leon')
