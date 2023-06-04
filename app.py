import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    st.title("Recuima")

    menu = ["Descripción del Proyecto", "Descripción del Dataset", "Documentación", "Equipo"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Descripción del Proyecto":
        st.subheader("Aprendizaje Automático orientado a la detección de factores de riesgo para pacientes de infarto")
        st.write("""
        Se tienen características médicas tomadas de más de 1000 pacientes de 4 hospitales distintos distribuidos del país y se desea hacer un estudio exhaustivo en esas 
        características para conocer cuáles podrían ser un factor decisivo para conservar en cada etapa la salud del paciente. Se emplea para esto distintos metodos de aprendizaje
        automático como Redes Neuronales Convolucionales y se hace un estudio de los resultados estadísticos obtenidos.
        """)

    elif choice == "Descripción del Dataset":
        st.subheader("Descripción del Dataset")
        st.write("""
        Se tiene un dataset de más de 1000 paciente de 4 hospitales distintos del país.
        """)

    elif choice == "Documentación":
        st.subheader("Documentación")
        st.write("""
        Aquí puedes proporcionar enlaces y descripciones a documentación relevante o escribir tu propia documentación.
        """)

    elif choice == "Equipo":
        st.subheader("Integrantes")

        col1, col2 = st.columns(2)

        with col1:
            st.image("picture/profile.png")  # actualiza con la ruta a la imagen o url
        with col2:
            st.markdown("""
            ### Josué Rodríguez  
            Email: [j.rodriguez@mail.com](mailto:j.rodriguez@mail.com)  
            GitHub: [jrodriguez](https://github.com/jrodriguez)  
            Telegram: [jrodriguezTelegram](https://t.me/jrodriguezTelegram)
            """)

        col1, col2 = st.columns(2)

        with col1:
            st.image("picture/profile.png")  # actualiza con la ruta a la imagen o url
        with col2:
            st.markdown("""
            ### Lázaro D. Apellido  
            Email: [email@dominio.com](mailto:email@dominio.com)  
            GitHub: [username](https://github.com/username)  
            Telegram: [usernameTelegram](https://t.me/usernameTelegram)
            """)

        # Agrega más bloques para más miembros del equipo...

        st.markdown("""
        ---
        ##### Copyright 
        Esta página fue creada por el equipo de Machine Learning de la Universidad de La Habana.
        """)

if __name__ == "__main__":
    main()