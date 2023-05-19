import streamlit as st
import models
import consulta
import time

zoo = models.Zoologico()
zoo.cargarInfo()
permiso = True

def alert(habitat):
    st.write('Alguna caracteristica del animal no coindicida con las del habitat')
    st.write(f'Recuerda que para ingresar un animal a {habitat.nombre}')
    st.write(f'Los animales debe caber en el espacio')
    dietas = habitat.dieta
    st.write(f'Deben ser {dietas}')
    especies = habitat.especies
    st.write(f'Y deben ser {especies}')
    time.sleep(3)
    st.experimental_rerun()


def procesar_informacion(nombre, edad, tamanio, dieta, especie, temperatura, salud, habitats, comidas_al_dia, horas_dormidas, horas_juego,vertebrado):
    habitat = consulta.buscar_habitat(habitats)

    permiso = habitat.agregar_animal(nombre=nombre,tamaño=tamanio,dieta=dieta,especie=especie)

    if permiso:
    
        if especie=="Mamiferos":
            nuevo_animal = models.Mamiferos(None,nombre,edad,tamanio,dieta,comidas_al_dia,horas_dormidas,horas_juego,temperatura,salud,habitats)
        if especie=="Insectos":
            nuevo_animal = models.Insectos(dic=None, nombre=nombre, edad=edad, tamaño=tamanio, dieta=dieta, comidas=comidas_al_dia,temperatura=temperatura,salud=salud,habitat=habitats)
        if especie=="Aves":
            nuevo_animal = models.Aves(dic=None, nombre=nombre, edad=edad, tamaño=tamanio, dieta=dieta, comidas=comidas_al_dia,dormir=horas_dormidas,temperatura=temperatura,salud=salud,habitat=habitats)
        if especie=="Reptiles":
            nuevo_animal = models.Reptiles(dic=None,nombre=nombre, edad=edad, tamaño=tamanio, dieta=dieta, comidas=comidas_al_dia, dormir=horas_dormidas,temperatura=temperatura,salud=salud,habitat=habitats)
        if especie=="Peces":
            nuevo_animal = models.Peces(dic = None, nombre=nombre, edad=edad, tamaño=tamanio, dieta=dieta, vertebrado = vertebrado, comidas=comidas_al_dia,temperatura=temperatura,salud=salud,habitat=habitats)
        if especie=="Anfibios":
            nuevo_animal = models.Anfibios(dic=None, nombre=nombre, edad=edad, tamaño=tamanio, dieta=dieta, comidas=comidas_al_dia, dormir=horas_dormidas,temperatura=temperatura,salud=salud,habitat=habitats)

        nuevo_animal.guardar_info()

        st.success(f'{nuevo_animal.nombre} agregado al habitat {habitats}')
        time.sleep(3.5)
        st.experimental_rerun()
    else:
        alert(habitat=habitat)

st.title("Formulario de animales")

# Campo Nombre
nombre = st.text_input("Nombre")

# Campo Edad
edad = st.number_input("Edad", min_value=0, max_value=100, step=1)

# Campo Tamaño
tamanio = st.radio("Tamaño", ["Pequeño", "Mediano", "Grande"])

# Campo Dieta
dieta = st.radio("Dieta", ["Carnivora", "Omnivora", "Vegetariana"])

# Campo Especie
especie = st.radio("Especie", ["Mamiferos", "Insectos", "Aves", "Peces", "Reptiles", "Anfibios"])

# Campo Temperatura
temperatura = st.radio("Temperatura", ["Frio", "Templado", "Tropical", "Calido", "Caliente"])

# Campo Salud
salud = st.radio("Salud", ["Saludable", "Enfermo", "En Recuperacion"])

vertebrado = ''

if especie == 'Peces':
    vertebrado = st.radio('Tipo',["Vertebrado","Invertebrado"])

# Campo Habitats
habitats = st.radio("Hábitats", options=zoo.get_habitats())

# Campo Comidas al día
comidas_al_dia = st.number_input("Comidas al dia", min_value=1, max_value=5, step=1)

# Campo Horas dormidas
# Campo Horas de juego
horas_dormidas =-1
horas_juego = -1

if especie == 'Mamiferos':
    horas_dormidas = st.number_input("Horas dormidas", min_value=1, max_value=10, step=1)
    horas_juego = st.number_input("Horas de juego", min_value=1, max_value=5, step=1)

elif especie == 'Anfibios' or especie == 'Aves' or especie == 'Reptiles':
    horas_dormidas = st.number_input("Horas dormidas", min_value=1, max_value=10, step=1)

# Botón Enviar
if st.button("Enviar"):
    # Llamar a la función para procesar la información
    procesar_informacion(nombre, edad, tamanio, dieta, especie, temperatura, salud, habitats, comidas_al_dia, horas_dormidas, horas_juego,vertebrado)

