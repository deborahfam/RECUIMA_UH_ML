import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )
image01 = 'picture/image01.png'
image02='picture/image02.png'
image03='picture/image03.png'
image04='picture/image04.png'


PAGES = {
    "Dataset original": "/Dataset_original",
    "Feature reduction": "/Feature_reduction",
    "Improved Dataset":"/Improved_Dataset",
    "Final Dataset":"/Final_Dataset",
}
st.set_page_config(page_title="RECUIMA", layout="wide")


st.sidebar.success("Datasets")
selection = st.sidebar.radio("", list(PAGES.keys()))

 # Create a function to display the selected page
def display_page(page):
    if page == "/Dataset_original":
        st.sidebar.success("Dataset original")
        st.sidebar.write('Falta de balance en los datos')
        st.sidebar.write('Correlación entre características')
        st.header("Características del Dataset original")

        st.markdown("""#### Falta de balance en los datos

El _dataset_ mostró un claro desbalance en los datos teniendo en cuenta el _feature_ objetivo, la cantidad de pacientes que no fallecen, luego de ingresar al hospital, es mucho mayor de los que sí lo hacen, en la muestra observada. Como se puede apreciar en la siguiente imagen:
""")
        st.image(image01)
        st.markdown("""
#### Correlación entre características:

En el _dataset_ original existen características que están estrechamente correlacionadas con otras, lo que significa que la información que brindan es redundante. Por lo tanto dichas características pueden ser eliminadas del _dataset_ para aligerar el peso del mismo sin sacrificar veracidad de los datos.
""")
        
        st.image(image02)
        st.markdown("""
Como se observa en la imagen anterior tanto la presion arterial sistólica como la diastólica están correlacionadas, por lo que se decidió eliminar la segunda del _dataset_. Lo mismo ocurre con la edad y la escala GRACE, por lo que se decidió eliminar la segunda del _dataset_.


Producto de la falta de datos en muchos de los features no se pudo realizar el PCA en el _dataset_ original.
        """)
        st.image(image03)
        st.markdown("""

Como se muestra en la imagen anterior existen datos demasiado dispersos para poder realizar esta prueba en el _dataset_, dado que el PCA no admite falta de datos. También por la ocurrencia de datos binarios y no binarios se necesita normalizar los datos para llevarlos a una métrica estándar.
Por otra parte se tomó medidas para reajustar el _dataset_ quitando los _features_ en los que faltaban datos. Como resultado de esta operación se obtuvo el [[Feature Reduction]].""")
    elif page == "/Feature_reduction":
        st.sidebar.success("Feature reduction")
        st.sidebar.write('Estrategia de completado fijo')
        st.header("Características del Dataset usando Feature Reduction")
        st.markdown("""Para un fácil manejo de la información, evitar la redundancia de los datos y eliminar todas aquellas características que se creían prescindibles en una primera instancia, el conjunto de datos original se redujo a una muestra de solo 18 características. 

Este completamiento se aplica al siguiente conjunto de características:

-   estado vital
-   edad
-   sexo
-   peso
-   hipertensión arterial
-   diabetes mellitus
-   tabaquismo
-   frecuencia cardíaca
-   presión arterial sistólica
-   hb
-   creatinina
-   ckmb
-   fibrilación auricular
-   insuficiencia renal crónica
-   ieca
-   furosemida
-   otros diuréticos
-   clopidogrel

Cabe mencionar que en este dataset persiste el problema de desbalance de los datos en cuanto al _feature_ objetivo. Problema con el cual se lidia posteriormente. Por otra parte con esta medida se soluciona el problema de dispersión de los datos.

#### Estrategia de completado fijo:

Los valores faltantes de las características se rellenan con valores predefinidos o promedios de una subpoblación (en el caso de nosotros extraídos de la documentación). En el caso de `ckmb` se llenó en función del `sexo` y el `infarto agudo miocardio` con los valores promedios de la documentación. El nivel de `ckmb` puede variar según el género y la condición de infarto de miocardio, y el uso de estos promedios específicos puede proporcionar una estimación más precisa de los valores faltantes. Para la `creatinina` se llenó con el mismo valor por defecto cubano para todos. Este enfoque asume que la creatinina tiene una distribución similar en toda la población, por lo que un valor constante es una buena estimación. Por último la `hb` se llenó en dependencia del sexo, pero con el valor por defecto cubano fijo. Este enfoque se basa en la suposición de que la hemoglobina puede variar según el sexo.

Para esto se buscó los valores por defecto de las siguientes características:

-   ckmb
-   creatinina
-   diabetes mellitus
-   frecuencia cardiaca
-   hb
-   hipertensión arterial
-   presión arterial sistólica
-   media de otros valores.

Como resultado de esta operación se obtiene el [[Improved Dataset]].""")
    elif page == "/Improved_Dataset":
        st.sidebar.success("Improved Dataset")
        st.header("Características del Dataset usando un primer aumento de features")
        st.markdown("""Para la confección de este _dataset_ se utilizó como base el de [[Feature Reduction]]. El cambio consiste en reincorporarle otras 5 características del [[Original Dataset]] las cuales también se consideraron relevantes luego de una investigación un poco más exhaustiva. 
Por otra parte es en este _dataset_ donde se normalizan los datos y además se analiza la distribución probabilística para poder trabajar con los modelos que se tenían pensados.
        """)
        st.image(image04)
        st.markdown("""
La imagen anterior muestra la distribución de los datos, de los cuales como se aprecia existen varios que distribuyen normal lo cual justifica el uso del modelo de ML **Gaussian Naive Bayes**.
Este _dataset_ es el que se utilizó en el [[Pipeline 1]].""")
    elif page == "/Final_Dataset":
        st.sidebar.success("Final Dataset")
        st.markdown("""
                    # Resumen

Este _dataset_ se construyó a partir del [[Improved Dataset]], agregando cinco características. 

## Características agregadas

**Tiempo Isquemia**:
La cardiopatía isquémica se produce cuando se obstruye una arteria del corazón. Si es de manera lenta, se habla de angina de pecho, si se tapona de forma rápida, es cuando se produce un infarto.

**SCACEST**:
El SCACEST es el término referido a “síndrome coronario agudo sin elevación de ST”, que abarca una variedad de síntomas clínicos que resultan de una isquemia miocárdica aguda como el infarto sin onda Q y la angina inestable (ausencia de elevación enzimática).

**Insuficiencia Cardiaca Congestiva**:
La insuficiencia cardíaca congestiva ocurre cuando el corazón no es capaz de bombear la sangre de manera eficaz. Esto produce que la sangre y los líquidos se acumulen en los pulmones, hígado y otros órganos, de modo que el corazón tiene que esforzarse más para bombear sangre al resto del cuerpo.

**Enfermedades Arterias Coronarias**:
Es el tipo más común de enfermedad cardiaca. Es la principal causa de muerte entre los hombres y las mujeres en los Estados Unidos. La EAC ocurre cuando las arterias que suministran la sangre al músculo cardíaco se endurecen y se estrechan.

**Infarto Miocardio Agudo**:
una de cada cinco personas que han sufrido un infarto, tendrá otro en un periodo de un año, aunque siga un tratamiento, ya que la mayoría de estos pacientes no adoptan medidas adecuadas.""")
display_page(PAGES[selection])