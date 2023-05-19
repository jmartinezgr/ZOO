import streamlit as st
import models
import consulta
import time


def accion(num,animal):
    if num==1:
        info = animal.comer("Comida")
        animal.guardar_info(tipo='u')
        return info
    if num == 2:
        info = animal.dormir()
        animal.guardar_info(tipo='u')
        return info
    if num == 3:
        info = animal.jugar()
        animal.guardar_info(tipo='u')
        return info

st.set_page_config(
    page_title="ZOO",
)

zoo = models.Zoologico()
zoo.cargarInfo()
    
st.title("Zoologico con python")
    
habitats = zoo.get_habitats()
cont = 0
cont_botones = 30
for habitat in habitats:
    cont+=1
    habitat_auxiliar = consulta.buscar_habitat(habitat)
    with st.expander(f'## {habitat}'):
        st.write("")
        st.write("")
        col1, col2 = st.columns([2, 1])
        with col1:
            if len(habitat_auxiliar.animales) >0:
                st.write(f'Estos son los animales en {habitat}')
            else:
                st.write(f'Aun no se a agregado animales en {habitat}')
        st.markdown("<hr>", unsafe_allow_html=True)
        for animal in habitat_auxiliar.animales:    
            col4,col5,col6 = st.columns([2,3,1])
            objeto = consulta.buscar_animal(animal)
            with col4:
                st.write(f'Nombre: {models.poner_enies(objeto.nombre)}')
                edad = objeto.edad
                st.write(f'Edad: {edad} años')
                dieta = objeto.dieta
                st.write(f'Dieta: {dieta}')
                especie = objeto.especie
                st.write(f'Especie: {especie}')
                
            mensaje = ''

            with col6:
                if st.button("Comer",key=cont_botones+1):
                    mensaje = accion(1,objeto)
                if st.button("Dormir",key=cont_botones+2):
                    mensaje = accion(2,objeto)
                if st.button("Jugar",key=cont_botones+3):
                    mensaje = accion(3,objeto)

                cont_botones+=3

            if mensaje:
                if mensaje[0]:
                    st.success(mensaje[1])
                else:
                    st.error(mensaje[1])
                time.sleep(3)
                mensaje = ""
                st.experimental_rerun()
            st.markdown("<hr>", unsafe_allow_html=True)
