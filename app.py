import streamlit as st

def main():
    st.title("Ejemplo de Expanders en Streamlit")
    
    # Expander 1
    with st.expander("Expander 1"):
        st.write("Contenido del Expander 1")
    
    # Expander 2
    with st.expander("Expander 2"):
        st.write("Contenido del Expander 2")
    
    # Expander 3 con contenido dinámico
    with st.expander("Expander 3"):
        opcion = st.radio("Selecciona una opción", ["Opción 1", "Opción 2"])
        st.write("Has seleccionado:", opcion)



if __name__ == "__main__":
    main()