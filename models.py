import json

class Zoologico:
    def __init__(self):
        self.tipos_habitats = ["Selvatico","Desertico","Polar","Acuatico"]
        self.habitats = []
        self.animales = []
        self.url = []

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