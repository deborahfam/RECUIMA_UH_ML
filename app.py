import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Establece la configuración de la página a wide (amplio)
#st.set_page_config(layout="wide")

#sección de imagenes
pipeline01_regresionLogistica = 'picture/pipeline01_regresionLogistica.jpg'
pipeline02_modelacc = 'picture/pipeline2_modelacc.jpg'
pipeline02_modelloss = 'picture/pipeline2_modelloss.jpg'


def main():
    
    st.title("Recuima")

    st.subheader("Aprendizaje Automático orientado a la detección de factores de riesgo para pacientes de infarto")
    st.markdown("""
        Se tienen características médicas tomadas de más de 1000 pacientes de 4 hospitales distintos distribuidos del país y se desea hacer un estudio exhaustivo en esas 
        características para conocer cuáles podrían ser un factor decisivo para conservar en cada etapa la salud del paciente. Se emplea para esto distintos métodos de aprendizaje
        automático como Redes Neuronales Convolucionales y se hace un estudio de los resultados estadísticos obtenidos.
        """)

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

    # elif choice == "Equipo":
    #     st.subheader("Integrantes")

    #     col1, col2 = st.columns(2)

    #     with col1:
    #         st.image("picture/profile.png")  # actualiza con la ruta a la imagen o url
    #     with col2:
    #         st.markdown("""
    #         ### Josué Rodríguez  
    #         Email: [j.rodriguez@mail.com](mailto:j.rodriguez@mail.com)  
    #         GitHub: [jrodriguez](https://github.com/jrodriguez)  
    #         Telegram: [jrodriguezTelegram](https://t.me/jrodriguezTelegram)
    #         """)

    #     col1, col2 = st.columns(2)

    #     with col1:
    #         st.image("picture/profile.png")  # actualiza con la ruta a la imagen o url
    #     with col2:
    #         st.markdown("""
    #         ### Lázaro D. Apellido  
    #         Email: [email@dominio.com](mailto:email@dominio.com)  
    #         GitHub: [username](https://github.com/username)  
    #         Telegram: [usernameTelegram](https://t.me/usernameTelegram)
    #         """)

    #     # Agrega más bloques para más miembros del equipo...

    #     st.markdown("""
    #     ---
    #     ##### Copyright 
    #     Esta página fue creada por el equipo de Machine Learning de la Universidad de La Habana.
    #     """
    st.subheader("Estado del arte")
    st.markdown("""
        
        El uso de machine learning en la medicina, especialmente en el campo de las afecciones cardíacas, ha experimentado un gran avance en los últimos años. Gracias al progreso en las técnicas de aprendizaje automático y al aumento en la capacidad computacional, se han abierto nuevas oportunidades de investigación en la modelización cardiovascular.
        Las aplicaciones de machine learning en afecciones cardíacas abarcan desde la predicción y diagnóstico de enfermedades cardíacas hasta la personalización de tratamientos y la identificación de factores de riesgo. Algunas de las técnicas más utilizadas en este campo incluyen redes neuronales artificiales (ANN), redes neuronales convolucionales (CNN), máquinas de vectores de soporte (SVM), árboles de decisión, bosques aleatorios y deep learning.
        El uso de machine learning en el diagnóstico y tratamiento de afecciones cardíacas permite a los médicos y profesionales de la salud tomar decisiones informadas y mejorar la atención al paciente.        
        
        - Redes neuronales artificiales (ANN): Las ANN son una de las técnicas más comunes utilizadas en la predicción de enfermedades cardíacas. Estos modelos pueden manejar datos no lineales y son capaces de aprender de los errores a través de un proceso de retropropagación. 

        - Redes neuronales convolucionales (CNN): Las CNN son una subcategoría de las redes neuronales que se utilizan comúnmente en el análisis de imágenes médicas. En el contexto de las enfermedades cardíacas, las CNN pueden ser utilizadas para analizar imágenes de electrocardiogramas (ECG) y ecocardiogramas para detectar signos de enfermedad cardíaca.

        - Máquinas de vectores de soporte (SVM): Las SVM son otra técnica comúnmente utilizada en la predicción de enfermedades cardíacas. Estos modelos son capaces de manejar datos de alta dimensión y pueden ser eficaces en la identificación de patrones complejos.

        - Árboles de decisión y bosques aleatorios: Estos modelos son útiles para identificar las características más importantes en la predicción de enfermedades cardíacas. Los bosques aleatorios, en particular, son eficaces para manejar datos de alta dimensión y pueden proporcionar una medida de la importancia de las características.

        - Deep Learning: El Deep Learning es una subcategoría del aprendizaje automático que utiliza redes neuronales con muchas capas (deep neural networks). Estos modelos son capaces de aprender características de alto nivel a partir de los datos y han demostrado ser eficaces en la predicción de enfermedades cardíacas.
        
        Actualmente existen trabajos realizados con los que se obtienen resultados satisfactorios para evitar la mortalidad en pacientes de infarto:
        - Un estudio de García-Ordás et al. (2023) publicado en la revista Multimedia Tools and Applications utilizó ANN para predecir la enfermedad cardíaca con una precisión del 83.5%.
        - "Machine learning prediction of mortality in Acute Myocardial Infarction." - Oliveira M, Seringa J, Pinto FJ, Henriques R, Magalhães T. (2023). Este estudio creó un modelo basado en aprendizaje automático para el análisis predictivo de la mortalidad en pacientes con infarto agudo de miocardio a la admisión, utilizando diferentes variables para analizar su impacto en los modelos predictivos.

        - "Prognostic Value of Machine-Learning-Based PRAISE Score for Ischemic and Bleeding Events in Patients With Acute Coronary Syndrome Undergoing Percutaneous Coronary Intervention." (2023). Este estudio presenta el PRAISE (Prediction of Adverse Events Following an Acute Coronary Syndrome) score, un modelo basado en aprendizaje automático para predecir la muerte por cualquier causa, infarto de miocardio y sangrado en el primer año en pacientes con síndrome coronario agudo.

        - "A Machine Learning-Based Applied Prediction Model for Identification of Acute Coronary Syndrome (ACS) Outcomes and Mortality in Patients during the Hospital Stay." (2023). Este estudio utilizó el conjunto de datos del Registro de Infarto Agudo de Miocardio de Corea (KAMIR-NIH), que contiene datos de 13,104 pacientes con 551 características. El rendimiento del modelo de aprendizaje automático fue comparado con otros modelos aplicados.

        - "Identification of Coronary Culprit Lesion in ST Elevation Myocardial Infarction by Using Deep Learning." (2023). Este estudio utilizó un modelo de aprendizaje profundo con una red neuronal convolucional para identificar la lesión culpable en pacientes con infarto de miocardio con elevación del segmento ST (STEMI).

        - "Comparison of conventional scoring systems to machine learning models for the prediction of major adverse cardiovascular events in patients undergoing coronary computed tomography angiography." (2022). Este estudio compara el rendimiento pronóstico de los sistemas de puntuación convencionales con un modelo de aprendizaje automático en la tomografía computarizada de coronarias para discriminar entre los pacientes con y sin eventos cardiovasculares adversos mayores.
        """)

    st.subheader("Completamiento de Datos")
    st.write("""
            El dataset obtenido para el desarrollo del proyecto tenía en algunas características datos faltantes ya fuera porque la medición de los datos no se hizo
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
            - hipertensión_arterial
            - diabetes_mellitus
            - tabaquismo
            - frecuencia_cardíaca
            - presión_arterial_sintólica
            - presión_arterial_diastolica
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
    st.subheader("Modelo SNN")
    st.markdown("""
                Uno de los modelos de Machine Learning utilizado es Redes Neuronales Secuenciales (SNN)
                """)
    st.write("""
            Las Redes Neuronales Secuenciales (SNN, por sus siglas en inglés) son un tipo de Redes Neuronales Artificiales (ANN, por sus siglas en inglés) que son particularmente 
            útiles para tratar con datos secuenciales o temporales. Sin embargo, en el contexto del código proporcionado, parece que se está utilizando una red neuronal artificial 
            estándar, no una red neuronal secuencial.

            En general, las redes neuronales, incluyendo las SNN, son útiles para tareas de predicción como la detección de enfermedades del corazón por varias razones:

            - Capacidad de manejar datos no lineales: Las enfermedades del corazón pueden ser el resultado de una combinación compleja y no lineal de diferentes factores de riesgo. Las redes neuronales son capaces de modelar estas relaciones no lineales.

            - Capacidad para aprender de grandes cantidades de datos: Las redes neuronales pueden aprender patrones complejos a partir de grandes cantidades de datos, lo que las hace adecuadas para tareas de clasificación y predicción.

            - Capacidad para manejar diferentes tipos de datos: Las redes neuronales pueden manejar diferentes tipos de datos, como datos numéricos, categóricos y de imagen.

            - Tolerancia al ruido: Las redes neuronales son robustas frente al ruido y a los datos faltantes, lo que puede ser útil en medicina donde los datos pueden ser ruidosos o incompletos.

           Por lo que estas son especialmente útiles cuando los datos tienen una estructura secuencial o temporal.""")
    
    st.markdown("""
                ### Metodología""")
    st.write("""
            Dataset: Los datos provienen del repositorio de aprendizaje automático de la UCI y también están disponibles en Kaggle.

            Evaluación: El modelo se evalúa en función de la matriz de confusión y la precisión de la predicción de si un paciente tiene o no una enfermedad del corazón.

            Características: Se realiza un análisis exploratorio de los datos, incluyendo visualizaciones y correlaciones entre las características.

            Modelado: Se utiliza una red neuronal artificial con tres capas ocultas. La red se entrena utilizando el optimizador Adam y la función de pérdida de entropía cruzada binaria. 
            La precisión se utiliza como métrica para evaluar el rendimiento del modelo.

            Experimentación: Se realizan varias pruebas y se ajustan los parámetros del modelo para mejorar su rendimiento.""")
    
    st.subheader("Pipelines")
    st.write("""
             Para la implementacion de los distintos modelos de machine learning se implementan pipelines.ipynb que es una manera secuencial organizada de guardar el testeo de los datos
             
             El proyecto contiene 15 pipelines los cuales vamos a explicar algunos:
             
             Pipeline 01:
             
             Se usa como dataset el primer "argumented_data" con los primeros 24 features que se eligieron los cuales están excentos de datos faltantes.
             Métodos utilizados para el análisis de datos:

            - Normalización de datos: Los datos se normalizan antes de ser utilizados para entrenar los modelos. Esto se hace para asegurar que todas las características tengan la misma escala y no sesguen el modelo.

            - Algoritmos de aprendizaje automático: Se utilizan varios algoritmos de aprendizaje automático, incluyendo SVM (Support Vector Machines), Naive Bayes, Random Forest, Logistic Regression, MLP (Multi-Layer Perceptron), y K-Nearest Neighbors.

            - Validación cruzada K-Fold: Para evaluar los modelos, se utiliza la validación cruzada K-Fold. En este caso, se utiliza una validación cruzada de 10 pliegues.

            ### Resultados obtenidos:
            Los resultados parecen variar dependiendo del modelo utilizado. Aquí hay algunos resultados destacados:

            - Modelo de Regresión Logística: Este modelo obtuvo una precisión del 89% con una puntuación media de validación cruzada de 0.878. La precisión, el recall y la puntuación F1 para las dos clases también se proporcionan en el artículo.
            """)
    st.image(pipeline01_regresionLogistica, caption='Regresion Logística', use_column_width=True)
    st.write("""
             Pipeline 02 y 03
             
             Se mejoran los resultados anteriores con el uso de "balance_wight" y se utiliza el agrupamiento de datos con stratifiedKFold.""")
    # Crea las columnas
    col1, col2 = st.columns(2)

    # Muestra las imágenes en sus respectivas columnas
    col1.image(pipeline02_modelacc, caption='Eficacia del Modelo', use_column_width=True)
    col2.image(pipeline02_modelloss, caption='Pérdida del Modelo', use_column_width=True)
    
    st.write("""
             Para los restantes pipeline se utilizan las mismas técnicas que para los anteriores pero con los dataset nuevos autocompletados
             - pipeline 011, 021, 031: data_augmentation dataset 1 
             - pipeline 012, 022, 032: data_augmentation dataset 2 
             - pipeline 013, 023, 033: data_augmentation dataset 3 
             - pipeline 014, 024, 034: autocomplete data           
             
             """)
    st.write("""
             ### Pipeline final:
             El pipeline final se presenta como una mezcla de estrategias utilizadas en otros. Aquí está un resumen de cada parte de este:

             1. **Preprocesamiento de Datos**: Los datos que se utilizan son los explicados anteriormente que contienen 24 características además de otras 5 que se consideraron relevantes según la bibliografía.
             2. **Escala de Características**: Las características continuas se escalan utilizando MinMaxScaler de sklearn, que transforma las características escalándolas a un rango dado, generalmente entre 0 y 1.
             3. **División de Datos**: Los datos se dividen luego en conjuntos de entrenamiento y prueba, con el 80% de los datos utilizados para el entrenamiento y el 20% utilizados para la prueba.
             4. **Entrenamiento y Evaluación del Modelo**: En los modelos utilizados se incluyen K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Regresión Logística, Gaussian Naive Bayes, Gradient Boosting Classification Tree basado en histograma y una Red Neuronal. Cada modelo se evalúa utilizando validación cruzada, puntuación de precisión, informe de clasificación y matriz de confusión. También se trazan curvas de aprendizaje para visualizar el rendimiento de los modelos.
             5. **Manejo de Datos Desbalanceados**: Para es desblance en los datos de cada clase a predecir (muertos y vivos) se realizan estrategias que suavizan esto. Esto se hace utilizando RandomOverSampler y BalancedBaggingClassifier de la biblioteca imbalanced-learn.
             6. **Optimización del Modelo**: Se utiliza validación cruzada estratificada y Análisis de Componentes Principales (PCA) para optimizar los modelos. Esta función también calcula e imprime las puntuaciones AUC, Precisión y Recall para cada pliegue y sus promedios.
             7. **Modelo de Aprendizaje Profundo**: Se incluye un modelo de aprendizaje profundo implementado con TensorFlow. El modelo es una red neuronal de avance con tres capas ocultas y una capa de abandono para prevenir el sobreajuste. El modelo se entrena utilizando el optimizador Adam y la pérdida de entropía cruzada binaria, y su rendimiento se evalúa utilizando precisión.
             
             Se obtuvieron los siguientes resultados en los diferentes modelos y tecnicas:
            
             1. **KNN**: Este modelo tiene una precisión del 87%, pero su capacidad para predecir correctamente la clase 1(Afectación al estado vital, muerto) es muy baja (recall del 3%). Esto sugiere que el modelo tiene dificultades para identificar correctamente los casos positivos en el conjunto de datos.
             2. **KNN con random OverSampler**: Aunque la precisión general disminuye al 77%, el recall para la clase 1 mejora significativamente al 42%. Esto indica que el oversampling puede ayudar a mejorar la capacidad del modelo para identificar la clase minoritaria.
             3. **Versión con BalanceBaggingClassifier de KNN**: Este modelo tiene una precisión del 73% y un recall para la clase 1 del 76%. Aunque la precisión es más baja, el modelo es mejor para identificar la clase minoritaria.
             4. **SVM**: Este modelo tiene una precisión del 81% y un recall para la clase 1 del 76%. Este es un buen rendimiento, especialmente en la identificación de la clase minoritaria.
             5. **Versión con BalanceBaggingClassifier de SVM**: Este modelo tiene una precisión del 80% y un recall para la clase 1 del 76%. Similar al modelo SVM, este modelo también tiene un buen rendimiento en la identificación de la clase minoritaria.
             6. **Regresión logística**: Este modelo tiene una precisión del 73% y un recall para la clase 1 del 86%. Aunque la precisión es más baja, el modelo es muy bueno para identificar la clase minoritaria.
             7. **Versión con BalanceBaggingClassifier de Regresión logística**: Este modelo tiene un rendimiento similar al modelo de regresión logística, con una precisión del 73% y un recall para la clase 1 del 86%.
             8. **Gaussian Naive Bayes**: Este modelo tiene una precisión del 75% y un recall para la clase 1 del 89%. Aunque la precisión es más baja, el modelo es excelente para identificar la clase minoritaria.
             9. **Versión con BalanceBaggingClassifier de Gaussian Naive Bayes**: Este modelo tiene una precisión del 87% y un recall para la clase 1 del 20%. Aunque la precisión es alta, el modelo tiene dificultades para identificar la clase minoritaria.
             10. **Histogram-based Gradient Boosting Classification Tree**: Este modelo tiene una precisión promedio del 90% y un recall promedio para la clase 1 del 32%. Este modelo tiene un buen rendimiento general, pero tiene dificultades para identificar la clase minoritaria.
             11. **Versión con BalanceBaggingClassifier de Regresión logística probada con Stratified K-Fold**: Las métricas en este caso presentan resultados un poco distintos una precisión promedio del 75% y un recall promedio para la clase 1 del 74%. Un rendimiento equilibrado en términos de precisión y recall.
             12. **Red neuronal**: Este modelo tiene una precisión del 83% y un recall para la clase 1 del 80%. Este modelo tiene un buen rendimiento equilibrado en términos de precisión y recall.
             
             En resumen, los modelos que no utilizan técnicas de balanceo de clases tienden a tener una precisión general más alta, pero un recall más bajo para la clase minoritaria. Esto sugiere que estos modelos pueden ser más útiles si el objetivo es minimizar la cantidad de falsos positivos, incluso a costa de perder algunos casos positivos.
             
             Por otro lado, los modelos que utilizan técnicas de balanceo de clases como Random OverSampler y BalanceBaggingClassifier tienden a tener un mejor rendimiento en términos de recall para la clase minoritaria. Sin embargo, estos modelos tambiéntienden a tener una precisión general más baja. Esto sugiere que estos modelos pueden ser más útiles si el objetivo es identificar la mayor cantidad posible de casos positivos, incluso a costa de una mayor cantidad de falsos positivos.
             
             El modelo de red neuronal parece tener un buen equilibrio entre precisión y recall, lo que sugiere que puede ser una buena opción si se busca un equilibrio entre la identificación de casos positivos y la minimización de falsos positivos.
             
             Debido al contexto médico en el que se presenta el proyecto, los modelos que poseen un mejor recall o aquellos suficientemente equilibrados deberían priorizarse por encima de una mejor precesión. Esto es común en medicina ya que es peor dejar pasar pacientes con la enfermedad que erróneamente diagnosticar con la enfermedad a pacientes sanos.
             """)
    st.subheader("Bibliografia")
    st.markdown("[García-Ordás et al., 2023, 'Heart disease risk prediction using deep learning techniques with feature augmentation', Multimedia Tools and Applications](https://buleria.unileon.es/handle/10612/15890)")
    st.markdown("[Machine learning prediction of mortality in Acute Myocardial Infarction](https://pubmed.ncbi.nlm.nih.gov/37072766/)")
    st.markdown("[Prognostic Value of Machine-Learning-Based PRAISE Score for Ischemic and Bleeding Events in Patients With Acute Coronary Syndrome Undergoing Percutaneous Coronary Intervention](https://pubmed.ncbi.nlm.nih.gov/36974761/)")
    st.markdown("[A Machine Learning-Based Applied Prediction Model for Identification of Acute Coronary Syndrome (ACS) Outcomes and Mortality in Patients during the Hospital Stay](https://pubmed.ncbi.nlm.nih.gov/36772390/)")
    st.markdown("[Identification of Coronary Culprit Lesion in ST Elevation Myocardial Infarction by Using Deep Learning](https://pubmed.ncbi.nlm.nih.gov/36654772/)")
    st.markdown("[Comparison of conventional scoring systems to machine learning models for the prediction of major adverse cardiovascular events in patients undergoing coronary computed tomography angiography](https://pubmed.ncbi.nlm.nih.gov/36386332/)")

if __name__ == "__main__":
    main()