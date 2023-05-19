import streamlit as st
import models

zoo = models.Zoologico()
zoo.cargarInfo()

def procesar_informacion(nombre, tipo_habitat, espacios_disponibles, temperatura, dieta, tipo_animal, especies):
    nuevo_habitat = models.Habitat(None,nombre,tipo_habitat,espacios_disponibles,temperatura,dieta,tipo_animal,especies,[])

    nuevo_habitat.cargar_habitat()

    st.experimental_rerun()

st.title("Formulario Habitats")

# Campo Nombre
nombre = st.text_input("Nombre")

# Campo Tipo de Habitat (Check button)
tipos_habitats = zoo.tipos_habitats
tipo_habitat = st.multiselect("Tipo de Habitat", options=tipos_habitats)

# Campo Espacios Disponibles
espacios_disponibles = st.number_input("Espacios disponibles", min_value=1, max_value=15, step=1)

# Campo Temperatura (Radio button)
opciones_temperatura = ["Frio", "Templado", "Tropical", "Calido", "Caliente"]
temperatura = st.radio("Temperatura", options=opciones_temperatura)

# Campo Dieta (Checkbox)
opciones_dieta = ["Carnivora", "Omnivora", "Vegetariana"]
dieta = st.multiselect("Dieta", options=opciones_dieta)

# Campo Tipo de Animal (Checkbox)
opciones_tipo_animal = ["Vertebrados", "Invertebrados"]
tipo_animal = st.multiselect("Tipo de Animal", options=opciones_tipo_animal)

# Campo Especies (Checkbox)
opciones_especies = ["Mamiferos", "Aves", "Insectos", "Reptiles", "Anfibios", "Peces"]
especies = st.multiselect("Especies", options=opciones_especies)

# Botón Enviar
if st.button("Enviar"):
    procesar_informacion(nombre, tipo_habitat, espacios_disponibles, temperatura, dieta, tipo_animal, especies)