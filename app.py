import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Establece la configuración de la página a wide (amplio)
st.set_page_config(layout="wide")

def main():
    
    st.title("Recuima")

    menu = [ "Descripción del Proyecto", "Descripción del Dataset", "Equipo"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Descripción del Proyecto":
        st.subheader("Aprendizaje Automático orientado a la detección de factores de riesgo para pacientes de infarto")
        st.markdown("""
        Se tienen características médicas tomadas de más de 1000 pacientes de 4 hospitales distintos distribuidos del país y se desea hacer un estudio exhaustivo en esas 
        características para conocer cuáles podrían ser un factor decisivo para conservar en cada etapa la salud del paciente. Se emplea para esto distintos metodos de aprendizaje
        automático como Redes Neuronales Convolucionales y se hace un estudio de los resultados estadísticos obtenidos.
        """)

    elif choice == "Descripción del Dataset":
        st.subheader("Descripción del Dataset")
        st.markdown("""
        Se tiene un dataset de más de 1300 paciente de 4 hospitales distintos del país con distintas características sobre los pacientes
        """)
        # Datos de ejemplo
        data = {
            'Característica': ['Edad', 'Peso', 'Talla', 'IMC', 'Sexo', 'Color de Piel', 'ASA', 'Betabloqueadores', 'Clopidogrel', 'Heparina', 'Estatinas', 'Estreptoquinasa Recombinante', 'Tiempo Puerta-Aguja', 'Reperfusión', 'Coronariografía', 'Tiempo Isquemia', 'Escala GRACE', 'Furosemida', 'Nitratos', 'Anticoagulantes', 'Anticálcicos', 'IECA', 'Otros Diuréticos', 'Lugar Trombolisis', 'AVC', 'MPT', 'VAM', 'MPP', 'Aminas', 'Balón', 'Atención Inicial', 'Horario Llegada', 'ECG Previo', 'SCACEST', 'Depresión ST', 'Depresión Onda T', 'Presión Arterial Sistólica', 'Presión Arterial Diastólica', 'Índice McMillan', 'Índice Killip', 'Frecuencia Cardíaca', 'Diabetes Mellitus', 'Insuficiencia Cardíaca Congestiva', 'Hipertensión Arterial', 'Hiperlipoproteinemia', 'Enfermedad Arterias Coronarias', 'Infarto Miocardio Agudo', 'Fibrilación Auricular', 'Intervención Coronaria Percutánea', 'CABG', 'Tabaquismo', 'Enfermedad Venosa Periférica', 'Insuficiencia Renal Crónica', 'Diálisis', 'Enfermedad Cerebro Vascular', 'Angina24h', 'Anemia', 'EPOC', 'FEVI', 'SHOCK', 'FIB AURIC', 'TV/FV/PCR', 'Isquemia', 'ICC', 'Arritmia', 'Colesterol', 'Creatinina', 'Filtrado Glomerular', 'Triglicéridos', 'Glicemia', 'ADA', 'Fracción Eyección', 'Leucocitos', 'Hemoglobina', 'CK', 'CKMB', 'Primera Asistencia Médica', 'Estado Vital'],
            'Descripción': ['Edad del paciente', 'Peso del paciente', 'Talla del paciente', 'Índice de Masa Corporal del paciente', 'Sexo del paciente', 'Color de piel del paciente', 'Escala ASA', 'Uso de betabloqueadores', 'Uso de clopidogrel', 'Uso de heparina', 'Uso de estatinas', 'Uso de estreptoquinasa recombinante', 'Tiempo desde la llegada hasta la administración del tratamiento', 'Si se realizó reperfusión', 'Si se realizó coronariografía', 'Tiempo desde el inicio de los síntomas hasta la llegada', 'Escala de riesgo GRACE', 'Uso de furosemida', 'Uso de nitratos', 'Uso de anticoagulantes', 'Uso de anticálcicos', 'Uso de IECA', 'Uso de otros diuréticos', 'Lugar donde se realizó la trombolisis', 'AVC', 'MPT', 'VAM', 'MPP', 'Uso de aminas', 'Uso de balón', 'Atención inicial', 'Horario de llegada', 'Existencia de ECG previo', 'SCACEST', 'Depresión del segmento ST', 'Depresión de la onda T', 'Presión arterial sistólica', 'Presión arterial diastólica', 'Índice McMillan', 'Índice Killip', 'Frecuencia cardíaca', 'Diabetes mellitus', 'Insuficiencia cardíaca congestiva', 'Hipertensión arterial', 'Hiperlipoproteinemia', 'Enfermedad de las arterias coronarias', 'Infarto agudo de miocardio', 'Fibrilación auricular', 'Intervención coronaria percutánea', 'CABG', 'Tabaquismo', 'Enfermedad venosa periférica', 'Insuficiencia renal crónica', 'Diálisis', 'Enfermedad cerebrovascular', 'Angina en las últimas 24 horas', 'Anemia', 'Enfermedad pulmonar obstructiva crónica', 'Fracción de eyección del ventrículo izquierdo', 'Shock', 'Fibrilación auricular', 'Taquicardia ventricular/fibrilación ventricular/paro cardiorrespiratorio', 'Isquemia', 'Insuficiencia cardíaca congestiva', 'Arritmia', 'Niveles de colesterol', 'Niveles de creatinina', 'Filtrado glomerular', 'Niveles de triglicéridos', 'Niveles de glucosa en sangre', 'ADA', 'Fracción de eyección', 'Niveles de leucocitos', 'Niveles de hemoglobina', 'Niveles de CK', 'Niveles de CKMB', 'Primera asistencia médica', 'Estado vital del paciente']
        }

        df = pd.DataFrame(data)

        # Crear la tabla
        st.table(df)

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
        
    doc_options = ["Seleccione","Estado del Arte", "Completamiento de Datos", "Pipelines"]
    doc_choice = st.sidebar.selectbox("Documentacion", doc_options)
    
    if doc_choice == "Estado del Arte":
        menu = "Seleccione"
        st.subheader("Estado del arte")
        st.markdown("""
        Completar.
        """)

    elif doc_choice == "Completamiento de Datos":
        st.subheader("Completamiento de Datos")
        st.write("""
            El dataset obtenido para el desarrollo del proyecto tenía en algunas características datos faltantes ya fuera porque la medicion de los datos no se hizo
            o porque el paciente no necesitaba esa medición. A raíz de eso se decidió utilizar métodos estadísticos para hacer completamiento de datos. 
            
            Se hizo dos tipos de modificaciones a los datos:
            - Completamiento de datos faltantes.
            - Aumento de datos.
            """)
        
        st.markdown("## Completamiento de datos faltantes.")
                        
        st.markdown("### Completamiento #1")
            
        st.write("""
            Este completamiento se aplica al siguiente conjunto de características:
            - estado_vital
            - edad
            - sexo
            - peso
            - hipertension_arterial
            - diabetes_mellitus
            - tabaquismo
            - frecuencia_cardiaca
            - presion_arterial_sistolica
            - presion_arterial_diastolica
            - hb
            - creatinina
            - ckmb
            - fibrilacion_auricular
            - insuficiencia_renal_cronica
            - ieca
            - furosemida
            - otros_diureticos
            - clopidogrel
            
            La elección de las mismas es basada en las características de la siguiente documentación (documentacion).
            En la misma se especifican características consideradas factores importantes a tener en cuenta, y luego que buscó un 
            correspondiente a esa característia en nuestro dataset.
            """) 
            
        st.markdown("#### Estrategia de completado fijo:")
        st.write("""
            Los valores faltantes de las características se rellenan con valores predefinidos o promedios de una subpoblación (en el caso de nosotros extraídos de la documentacion).
            
            - `ckmb` se llenó en función del 'sexo' y el 'infarto_agudo_miocardio' con los valores promedios de la documentación. El nivel de 'ckmb' puede variar según el género y la condición de infarto de miocardio, y el uso de estos promedios específicos puede proporcionar una estimación más precisa de los valores faltantes.
            - `creatinina` se llenó con el mismo valor por defecto cubano para todos. Este enfoque asume que la creatinina tiene una distribución similar en toda la población, por lo que un valor constante es una buena estimación.
            - `hb` se llenó en dependencia del sexo, pero con el valor por defecto cubano fijo. Este enfoque se basa en la suposición de que la hemoglobina puede variar según el sexo.

            Para esto se buscó los valores por defecto de las siguientes características:
            
            - ckmb
            - creatinina
            - diabetes mellitus
            - frecuencia cardiaca
            - hb
            - hipertension arterial
            - presion arterial diastolica
            - presion arterial sistolica
            - media de otros valores.
            """)
        st.markdown("#### Estrategia de completado con distribución normal:")
        st.write("""
            Los valores faltantes se llenan utilizando una distribución normal con media y desviación estándar predefinidas. Muchas características en los datos médicos siguen una distribución normal, por lo que esta puede ser una buena estrategia para llenar los valores faltantes.
            En este caso, '
            - `hb` se llenó en dependencia del sexo, con una distribución normal con media igual al valor por defecto cubano, y desviación estándar 7.
        """)
        st.markdown("#### Estrategia de completado utilizando valores promedios de datos reales sin anormalidades:")
        st.write("""
            Los valores faltantes se llenan utilizando los valores promedios de los datos existentes sin anormalidades. 
            En este caso:
            - `ckmb` se llenó en función del 'infarto_agudo_miocardio', con los valores promedios de los datos reales sin anormalidades. Para esto se utilizó una estrategia de eliminación de datos atípicos utilizando la desviación estándar.
            En este método, normalmente se consideran como atípicos los valores que caen fuera de 3 desviaciones estándar de la media. 

            La razón para elegir 3 desviaciones estándar se basa en la regla empírica (o regla 68-95-99.7) en estadísticas. Según esta regla, para una distribución normal, aproximadamente el 99.7% de los datos se encontrarán dentro de 3 desviaciones estándar de la media. Entonces, los valores que caen fuera de este rango son extremadamente raros bajo la suposición de normalidad y, por lo tanto, se pueden considerar valores atípicos.
            Finalmente, para el conjunto de características 02, se seleccionaron todas las características que tienen más de 1300 datos completos y se eliminaron las filas con datos incompletos. Este enfoque es sencillo y no introduce ninguna suposición adicional, pero puede resultar en la pérdida de algunas muestras de datos.
        """)
        st.markdown("### Completamiento #2")
        st.write(""" 
            Para este completamiento lo que se hizo fue una eliminacion por filas de aquellos que tuvieran datos incompletos para más de 1300 datos. De esta reducción nos quedamos con 62 caracteristicas.
            Luego a estos datos se le aplica relleno de datos faltantes de la fomra que estabamos trabajando anteriormente:
            
            - Media total cubana de creatinina.
            - Media por sexos, cubana de hemoblogina con distribución normal.
            - Media por cuadro de infarto, según medias de datos sin valores atípicos, de cmkb.
            
         """)
        
        st.markdown("## Aumento de datos")
        st.write("""
                En muchos problemas de aprendizaje automático, especialmente en los problemas de clasificación binaria, los datos pueden estar desequilibrados. Esto significa que hay más ejemplos de una clase que de otra.
                Este desequilibrio en los datos puede llevar a problemas en el modelo de aprendizaje automático, ya que el modelo puede sesgarse hacia la clase con más ejemplos. Por lo tanto, puede tener un rendimiento pobre cuando intenta predecir la clase minoritaria (en este caso, los pacientes que fallecieron).
                Una de las maneras de manejar este desequilibrio es mediante el "ampliado de data" o "data augmentation". En este proceso, se crean nuevos ejemplos de la clase minoritaria añadiendo un "ruido" a los ejemplos existentes. Esto puede ayudar a equilibrar los datos y a mejorar el rendimiento del modelo en la clase minoritaria.
                
                ```py
                "edad": [3]
                "peso":  [5]
                "frecuencia_cardiaca":[4]
                "presion_arterial_sistolica": [10,60]
                "presion_arterial_diastolica": [10,30]
                "hb":  [3,1]
                "creatinina": [3]
                "ckmb":  [5,1]
                ```
        """)

if __name__ == "__main__":
    main()