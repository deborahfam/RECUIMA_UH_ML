import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )


st.set_page_config(page_title="RECUIMA", layout="wide")


st.sidebar.success("Datos")
st.markdown("""
            # Descripción de los Datos de Entrenamiento

El primer y principal problema al que nos enfrentamos fue con el conjunto de datos, el cual tenía varias complicaciones:  

- Exceso de datos faltantes:  
    De $78$ características hay $22$ características con datos faltantes, lo que representa un $28.20\%$ del total de características. Además de $1353$ registros de pacientes, solo hay $246$ con todos los datos lo cuál representa un $18.18\%$.
- Errores en varios datos:  
    Cuando los médicos traspasaron los datos en físico a digital pudieron cometer algunos errores accidentalmente. Por ejemplo
- Desbalance entre clases:  
    Como el objetivo de este proyecto es predecir el estado del paciente que ingresa con problemas cardiológicos hay $2$ clases principales que nos interesan: los pacientes vivos, y los pacientes muertos. Sin embargo tanto en los datos de entrenamiento como en los de prueba hay un gran desvalance. Mientras se tiene registrados $1215$ los vivos, hay solo $138$ muertos, lo cual representa un $89.80\%$ y un $10.19\%$ respectivamente del total de datos.
- Escasez de datos:  
    De por sí, contamos con $1353$ datos de entrenamiento lo cual es relativamente poco para la cantidad usual que se usa para entrenar. Si a esto y el punto anterior sumamos que de los vivos hay $230$ que tienen todos sus datos completos y de los muertos solamente hay $16$ en estas condiciones entonces nos quedamos sin prácticamente datos para entrenar nuestros modelos.  

A continuación se muestran las estadísticas basicas del conjunto de datos para entrenamiento:

|                                   |   count |          mean |         std |     min |     25% |      50% |      75% |      max |
|:----------------------------------|--------:|--------------:|------------:|--------:|--------:|---------:|---------:|---------:|
| edad                              |    1353 |   66.221      |  12.6557    |  13     |  57     |   67     |   75     |   98     |
| peso                              |    1353 |   73.0266     |  11.9829    |  40     |  65     |   72     |   80     |  150     |
| talla                             |    1353 |  168.055      |   5.86377   | 120     | 165     |  168     |  172     |  190     |
| imc                               |    1353 |   25.7934     |   3.68674   |  16.135 |  23.121 |   25.535 |   28.082 |   58.273 |
| sexo                              |    1353 |    0.678492   |   0.467228  |   0     |   0     |    1     |    1     |    1     |
| color_piel                        |    1353 |    0.900961   |   0.298825  |   0     |   1     |    1     |    1     |    1     |
| asa                               |    1340 |    5.04403    |   5.17407   |   0     |   2     |    4     |    5     |   72     |
| betabloqueadores                  |    1185 |   24.9409     |  20.2011    |   0     |  12     |   24     |   24     |   99     |
| clopidogrel                       |    1353 |    0.961567   |   0.192311  |   0     |   1     |    1     |    1     |    1     |
| heparina                          |    1353 |    0.992609   |   0.0856842 |   0     |   1     |    1     |    1     |    1     |
| estatinas                         |    1353 |    0.978566   |   0.144879  |   0     |   1     |    1     |    1     |    1     |
| estreptoquinasa_recombinante      |    1353 |    0.503326   |   0.500174  |   0     |   0     |    1     |    1     |    1     |
| tiempo_puerta_aguja               |     681 |   94.9985     |  71.8521    |   5     |  60     |   60     |  120     |  700     |
| reperfusion                       |    1353 |    0.118995   |   0.323902  |   0     |   0     |    0     |    0     |    1     |
| coronariografia                   |    1353 |    0.0421286  |   0.200957  |   0     |   0     |    0     |    0     |    1     |
| tiempo_isquemia                   |    1241 |  348.645      | 428.092     |   0     | 150     |  240     |  420     | 9999     |
| escala_grace                      |    1333 |  110.651      |  26.4535    |  34     |  89     |  110     |  128     |  190     |
| furosemida                        |    1353 |    0.182557   |   0.386446  |   0     |   0     |    0     |    0     |    1     |
| nitratos                          |    1353 |    0.431633   |   0.495487  |   0     |   0     |    0     |    1     |    1     |
| anticoagulantes                   |    1353 |    0.209904   |   0.40739   |   0     |   0     |    0     |    0     |    1     |
| anticalcicos                      |    1353 |    0.105691   |   0.307555  |   0     |   0     |    0     |    0     |    1     |
| ieca                              |    1353 |    0.872136   |   0.334062  |   0     |   1     |    1     |    1     |    1     |
| otros_diureticos                  |    1353 |    0.515152   |   0.499955  |   0     |   0     |    1     |    1     |    1     |
| lugar_trombolisis                 |    1353 |    0.264597   |   0.441282  |   0     |   0     |    0     |    1     |    1     |
| avc                               |     966 |    0.120083   |   0.325227  |   0     |   0     |    0     |    0     |    1     |
| mpt                               |     966 |    0.0248447  |   0.155732  |   0     |   0     |    0     |    0     |    1     |
| vam                               |     966 |    0.0424431  |   0.201702  |   0     |   0     |    0     |    0     |    1     |
| mpp                               |     966 |    0.00621118 |   0.0786066 |   0     |   0     |    0     |    0     |    1     |
| aminas                            |     966 |    0.0890269  |   0.28493   |   0     |   0     |    0     |    0     |    1     |
| balon                             |     966 |    0          |   0         |   0     |   0     |    0     |    0     |    0     |
| atencion_inicial                  |    1353 |    0.492979   |   0.500136  |   0     |   0     |    0     |    1     |    1     |
| horario_llegada                   |    1353 |    0.716925   |   0.450659  |   0     |   0     |    1     |    1     |    1     |
| ecg_previo                        |    1353 |    0.652624   |   0.476313  |   0     |   0     |    1     |    1     |    1     |
| scacest                           |    1353 |    0.876571   |   0.329051  |   0     |   1     |    1     |    1     |    1     |
| depresion_st                      |    1353 |    0.71323    |   0.45242   |   0     |   0     |    1     |    1     |    1     |
| depresion_ondat                   |    1353 |    0.187731   |   0.390642  |   0     |   0     |    0     |    0     |    1     |
| presion_arterial_sistolica        |    1353 |  125.937      |  22.9879    |   0     | 120     |  130     |  130     |  240     |
| presion_arterial_diastolica       |    1353 |   74.7007     |  14.0609    |   0     |  70     |   70     |   80     |  130     |
| indice_mkillip                    |    1353 |    0.776792   |   0.41655   |   0     |   1     |    1     |    1     |    1     |
| indice_killip                     |    1353 |    0.831486   |   0.374461  |   0     |   1     |    1     |    1     |    1     |
| frecuencia_cardiaca               |    1353 |   84.8537     |  14.9467    |  30     |  78     |   86     |   88     |  180     |
| diabetes_mellitus                 |    1353 |    0.2949     |   0.456167  |   0     |   0     |    0     |    1     |    1     |
| insuficiencia_cardiaca_congestiva |    1353 |    0.0177384  |   0.132048  |   0     |   0     |    0     |    0     |    1     |
| hipertension_arterial             |    1353 |    0.849224   |   0.357963  |   0     |   1     |    1     |    1     |    1     |
| hiperlipoproteinemia              |    1353 |    0.0635625  |   0.244062  |   0     |   0     |    0     |    0     |    1     |
| enfermedad_arterias_coronarias    |    1353 |    0.322986   |   0.46779   |   0     |   0     |    0     |    1     |    1     |
| infarto_miocardio_agudo           |    1353 |    0.103474   |   0.304689  |   0     |   0     |    0     |    0     |    1     |
| fibrilacion_auricular             |    1353 |    0.0155211  |   0.123659  |   0     |   0     |    0     |    0     |    1     |
| intervencion_coronaria_percutanea |    1353 |    0.0347376  |   0.183182  |   0     |   0     |    0     |    0     |    1     |
| cabg                              |    1353 |    0.00813008 |   0.0898329 |   0     |   0     |    0     |    0     |    1     |
| tabaquismo                        |    1353 |    0.478197   |   0.499709  |   0     |   0     |    0     |    1     |    1     |
| enfermedad_venosa_periferica      |    1353 |    0.0421286  |   0.200957  |   0     |   0     |    0     |    0     |    1     |
| insuficiencia_renal_cronica       |    1353 |    0.0325203  |   0.177443  |   0     |   0     |    0     |    0     |    1     |
| dialisis                          |    1353 |    0.00591279 |   0.0766953 |   0     |   0     |    0     |    0     |    1     |
| enfermedad_cerebro_vascular       |    1353 |    0.0332594  |   0.17938   |   0     |   0     |    0     |    0     |    1     |
| angina24h                         |    1353 |    0.187731   |   0.390642  |   0     |   0     |    0     |    0     |    1     |
| anemia                            |    1353 |    0.0221729  |   0.1473    |   0     |   0     |    0     |    0     |    1     |
| epoc                              |    1353 |    0.0332594  |   0.17938   |   0     |   0     |    0     |    0     |    1     |
| FEVI                              |    1353 |    0.210643   |   0.407916  |   0     |   0     |    0     |    0     |    1     |
| SHOCK                             |    1353 |    0.0702143  |   0.255602  |   0     |   0     |    0     |    0     |    1     |
| FIB AURIC                         |    1353 |    0.0325203  |   0.177443  |   0     |   0     |    0     |    0     |    1     |
| TV/FV/PCR                         |    1353 |    0.09017    |   0.286531  |   0     |   0     |    0     |    0     |    1     |
| Isquemia                          |    1353 |    0.207687   |   0.405801  |   0     |   0     |    0     |    0     |    1     |
| ICC                               |    1353 |    0.277162   |   0.447763  |   0     |   0     |    0     |    1     |    1     |
| Arritmia                          |    1353 |    0.124908   |   0.330736  |   0     |   0     |    0     |    0     |    1     |
| colesterol                        |    1272 |    4.76722    |   1.10904   |   0.5   |   4.1   |    4.8   |    5.425 |   10     |
| creatinina                        |    1333 |  103.32       |  59.8738    |  38     |  78     |   89     |  113     | 1036     |
| filtrado_glomerular               |    1333 |   65.3797     |  24.8433    |   3.115 |  46.987 |   64.438 |   82.524 |  179.424 |
| trigliceridos                     |    1212 |    1.3113     |   0.720844  |   0     |   0.9   |    1.2   |    1.5   |    9     |
| glicemia                          |    1319 |    7.59568    |   3.5014    |   3.3   |   5.5   |    6.4   |    8.4   |   43     |
| ada                               |    1353 |    0.487066   |   0.500017  |   0     |   0     |    0     |    1     |    1     |
| fraccion_eyeccion                 |    1264 |   46.2389     |   8.16961   |  20     |  42     |   46     |   52     |   79     |
| leuco                             |     968 |    9.65661    |   5.51848   |   5.2   |   8.2   |    9.4   |   10.3   |  110.2   |
| hb                                |    1088 |  123.79       |  26.9165    |   8     | 125     |  132     |  134     |  238     |
| ck                                |     789 | 1212.45       | 730.362     |   1     | 805     | 1125     | 1529     | 3999     |
| ckmb                              |     802 |  144.471      | 113.736     |   0     |  85     |  120.5   |  165     |  960     |
| primera_asistencia_medica         |    1308 |  198.576      | 219.12      |   1     |  60     |  120     |  180     | 1080     |
| estado_vital                      |    1353 |    0.101996   |   0.302754  |   0     |   0     |    0     |    0     |    1     |

Además en la siguiente tabla mostramos la cantidad de datos que faltan por cada una de las $22$ características con valores faltantes:

|   Características con datos faltantes  | Cant. |
|:--------------------------|----:|
| asa                       |  13 |
| betabloqueadores          | 168 |
| tiempo_puerta_aguja       | 672 |
| tiempo_isquemia           | 112 |
| escala_grace              |  20 |
| avc                       | 387 |
| mpt                       | 387 |
| vam                       | 387 |
| mpp                       | 387 |
| aminas                    | 387 |
| balon                     | 387 |
| colesterol                |  81 |
| creatinina                |  20 |
| filtrado_glomerular       |  20 |
| trigliceridos             | 141 |
| glicemia                  |  34 |
| fraccion_eyeccion         |  89 |
| leuco                     | 385 |
| hb                        | 265 |
| ck                        | 564 |
| ckmb                      | 551 |
| primera_asistencia_medica |  45 |

# Selección de las características

Nuestro conjunto de datos contiene 78 características, sin embargo aunque los doctores implicados en el estudio indican que todos en gran o menor medida influyen en la determinación del `estado_vital` del paciente, como parte de nuestros objetivos está también reconocer, cuáles podrían ser lasc caraterísticas más significativas e influyentes en esta clasificación. Por lo tanto decidimos ir trabajando con un subconjunto de estas características para ir incorporando nuevas poco a poco, en la medida que mejoren los resultados obtenidos.

## Vector de Características 1

Las primeras características que tuvimos en cuenta fueron las utilizadas en el artículo [**1**]. En este se utilizan varios técnicas de Machine Learning para predecir la mortalidad de pacientes ingresados en hospitales por problemas cardíacos. En este se obtienen los siguientes resultados muy buenos resultados finales.

Debido a esto es que decidimos utilizar las características seleccionadas en este artículo para comenzar nuestro estudio. Estas fueron:  

| Característica | Nombre en el conjunto de datos |
|:---------------|--------------------------------:|
| Estado Vital                                          | 'estado_vital'                  |
| Edad                                                  | 'edad'                          |
| Sexo                                                  | 'sexo'                          |
| Peso                                                  | 'peso'                          |
| Hipertensión Arterial                                 | 'hipertension_arterial'         |
| Diabetes                                              | 'diabetes_mellitus'             |
| Tabaquismo                                            | 'tabaquismo'                    |
| Frecuencia Cardiaca                                   | 'frecuencia_cardiaca'           |
| Presión Arterial Sistólica                            | 'presion_arterial_sistolica',   |
| Presión Arterial Diastólica                           | 'presion_arterial_diastolica',  |
| Hemoglobina                                           | 'hb'                            |
| Creatinina                                            | 'creatinina'                    |
| Prueba de Creatina Quinasa                            | 'ckmb'                          |
| Fibrilación Arterial                                  | 'fibrilacion_auricular'         |
| Insuficiencia Renal                                   | 'insuficiencia_renal_cronica'   |
| Tratamiento con Inhibidores de la enzima angiotensina | 'ieca'                          |
| Tratamiento con Furosemida                            | 'furosemida'                    |
| Tratamiento con otros diureticos                      | 'otros_diureticos'              |
| Tratamiento con clopidogrel                           | 'clopidogrel'                   |

Sin embargo, hay otras características en el artículo pero que no tenemos en nuestros datos y no se pudo incorporar. Estas son:

- Troponina T
- Bloqueo de rama izquierda
- Bloqueo de rama derecha
- Tratamiento con aspirina

## Vector de Características 2

El segundo vector de características se hizo seleccionando 5 nuevas características del conjunto de datos, pero estudiando su influencia con la mortalidad por problemas cardíacos. Estas características fueron:

| Característica  | Nombre en el conjunto de datos  |
|:----------------|--------------------------------:|
| Triglicéridos   | 'trigliceridos' |
| Glicemia        | 'glicemia'      |
| Colesterol      | 'colesterol'    |
| Escala de Grace | 'escala_grace'  |
| Dialisis        | 'dialisis'      |

Para una descripción más detallada referirse a la sección Descripción de algunas caracterísitcas.


## Vector de Características 3

Y finalmente el último vector de características se hizo seleccionando otras 5 nuevas características del conjunto de datos. Estas características fueron:

| Característica            | Nombre en el conjunto de datos         |
|:--------------------------|---------------------------------------:|
| [PONNNNNNNNNNNEEEEEEER]   | 'tiempo_isquemia'                      |
| Glicemia                  | 'scacest'                              |
| Colesterol                | 'insuficiencia_cardiaca_congestiva'    |
| Enfermedad Coronarias     | 'enfermedad_arterias_coronarias'       |
| Infarto                   | 'infarto_miocardio_agudo'              |

Para una descripción más detallada referirse a la sección Descripción de algunas características.

# Tratamiento de los Datos

Debido a la mala calidad de los datos debemos aplicar técnicas para mejorar el conjunto de datos para eliminar los aspectos negativos antes mencionados. Usaremos varias técnicas dentro de dos categorías: **imputación** y **aumento**. Como sabemos que los resultados de nuestros algoritmos va a pedender en gran medida de la calidad del conjunto de datos entonces nos vemos en la necesidad de crear distintos de estos conjuntos e ir probando la efectividad de cada uno.

## Imputación de datos

Con este tipo de técnicas lo que se hace es rellenar los datos faltantes, mientras que lo que varía es la forma en que se rellenan esos datos. A continuación iremos explicando las diferentes formas en las que se fueron rellenando los valores faltantes.

### Imputación 1

Considerando el **Vector de Características 1**, decidimos rellenar valores de algunas de las características basados en los valores promedios atendiendo ciertos criterios y particularidades.

En [**1**] se encuentra una tabla con los promedios de las características que son utilizadas en este. Incluída aquellas que son categóricas. Entonces se utilizó el valor promedio de `ckmb` que se mostraba para rellenar los valores faltantes, sin embargo no fue este valor crudo el que se utilizó, sino que se tuvo en cuenta el `sexo` e `infarto_miocardio_agudo` para rellenar cada dato. Esto se debe a que estadísticamente categorizando por sexo e infarto, las medias de las pruebas CK-MB  son distintas, y sus estadísticos están recogidos también en el artículo, como se muestra a continuación:  

| Total con Infarto | Mujeres con Infarto | Hombres con Infarto | Total sin Infarto | Mujeres sin Infarto | Hombres sin Infarto |
|:------------------|---------------------|---------------------|-------------------|---------------------|---------------------|
| 197.37            | 184.70              | 204.39              | 52.57             | 47.39               | 56.28               |

El principal inconveniente de esto es que estos datos no son cubanos, por lo que su valor puede diferir mucho con la realidad de nuestro país, lo cual se verá más adelante.

Por otra parte se rellenó la `creatinina` con el valor promedio que se conocía internacionalmente [**3**] cuya media era $112.5$. Y por último la hemoglobina (`hb`) se rellenó con su valor promedio atendiendo el sexo del paciente ya que se sabe que hay diferencias estadísticas [**2**]; estos valores fueron $130$ para las mujeres y $150$ para los hombres.

A continuación se muestra el análisis estadístico del conjunto luego de la imputación:

|                             |   count |        mean |       std |   min |   25% |   50% |   75% |   max |
|:----------------------------|--------:|------------:|----------:|------:|------:|------:|------:|------:|
| estado_vital                |    1353 |   0.101996  |  0.302754 |     0 |     0 |     0 |   0   |     1 |
| edad                        |    1353 |  66.221     | 12.6557   |    13 |    57 |    67 |  75   |    98 |
| sexo                        |    1353 |   0.678492  |  0.467228 |     0 |     0 |     1 |   1   |     1 |
| peso                        |    1353 |  73.0266    | 11.9829   |    40 |    65 |    72 |  80   |   150 |
| hipertension_arterial       |    1353 |   0.849224  |  0.357963 |     0 |     1 |     1 |   1   |     1 |
| diabetes_mellitus           |    1353 |   0.2949    |  0.456167 |     0 |     0 |     0 |   1   |     1 |
| tabaquismo                  |    1353 |   0.478197  |  0.499709 |     0 |     0 |     0 |   1   |     1 |
| frecuencia_cardiaca         |    1353 |  84.8537    | 14.9467   |    30 |    78 |    86 |  88   |   180 |
| presion_arterial_sistolica  |    1353 | 125.937     | 22.9879   |     0 |   120 |   130 | 130   |   240 |
| presion_arterial_diastolica |    1353 |  74.7007    | 14.0609   |     0 |    70 |    70 |  80   |   130 |
| hb                          |    1353 | 127.637     | 25.7022   |     8 |   127 |   133 | 135   |   238 |
| creatinina                  |    1353 | 103.455     | 59.4396   |    38 |    78 |    89 | 113   |  1036 |
| ckmb                        |    1353 | 154.461     | 92.6681   |     0 |    95 |   171 | 184.7 |   960 |
| fibrilacion_auricular       |    1353 |   0.0155211 |  0.123659 |     0 |     0 |     0 |   0   |     1 |
| insuficiencia_renal_cronica |    1353 |   0.0325203 |  0.177443 |     0 |     0 |     0 |   0   |     1 |
| ieca                        |    1353 |   0.872136  |  0.334062 |     0 |     1 |     1 |   1   |     1 |
| furosemida                  |    1353 |   0.182557  |  0.386446 |     0 |     0 |     0 |   0   |     1 |
| otros_diureticos            |    1353 |   0.515152  |  0.499955 |     0 |     0 |     1 |   1   |     1 |
| clopidogrel                 |    1353 |   0.961567  |  0.192311 |     0 |     1 |     1 |   1   |     1 |

### Imputación 2

Esta imputación fue atendiendo a las mismas características escogidas anteriormente pero con un detalle importante. Esta vez la hemoglobina se fue rellenando atendiendo un intervalo, ya que normalente se suele indicar que un paciente promedio tiene su hemoglobina bien si está entre cierto intervalo. Además de la forma anterior podía existir más posibilidad de repetir algún registro lo cual puede a la larga repercutir en que nuestros algoritmos se sobrentrenen. Por lo tanto esta vez la `hb` fue rellenada de forma aleatoria con las mismas medias dichas en la sección anterior y desviación $7$.

A continuación los estadísticos del nuevo conjunto de datos:

|                             |   count |        mean |       std |   min |   25% |   50% |   75% |   max |
|:----------------------------|--------:|------------:|----------:|------:|------:|------:|------:|------:|
| estado_vital                |    1353 |   0.101996  |  0.302754 |     0 |     0 |     0 |   0   |     1 |
| edad                        |    1353 |  66.221     | 12.6557   |    13 |    57 |    67 |  75   |    98 |
| sexo                        |    1353 |   0.678492  |  0.467228 |     0 |     0 |     1 |   1   |     1 |
| peso                        |    1353 |  73.0266    | 11.9829   |    40 |    65 |    72 |  80   |   150 |
| hipertension_arterial       |    1353 |   0.849224  |  0.357963 |     0 |     1 |     1 |   1   |     1 |
| diabetes_mellitus           |    1353 |   0.2949    |  0.456167 |     0 |     0 |     0 |   1   |     1 |
| tabaquismo                  |    1353 |   0.478197  |  0.499709 |     0 |     0 |     0 |   1   |     1 |
| frecuencia_cardiaca         |    1353 |  84.8537    | 14.9467   |    30 |    78 |    86 |  88   |   180 |
| presion_arterial_sistolica  |    1353 | 125.937     | 22.9879   |     0 |   120 |   130 | 130   |   240 |
| presion_arterial_diastolica |    1353 |  74.7007    | 14.0609   |     0 |    70 |    70 |  80   |   130 |
| hb                          |    1353 | 127.646     | 25.962    |     8 |   126 |   133 | 135   |   238 |
| creatinina                  |    1353 | 103.455     | 59.4396   |    38 |    78 |    89 | 113   |  1036 |
| ckmb                        |    1353 | 154.461     | 92.6681   |     0 |    95 |   171 | 184.7 |   960 |
| fibrilacion_auricular       |    1353 |   0.0155211 |  0.123659 |     0 |     0 |     0 |   0   |     1 |
| insuficiencia_renal_cronica |    1353 |   0.0325203 |  0.177443 |     0 |     0 |     0 |   0   |     1 |
| ieca                        |    1353 |   0.872136  |  0.334062 |     0 |     1 |     1 |   1   |     1 |
| furosemida                  |    1353 |   0.182557  |  0.386446 |     0 |     0 |     0 |   0   |     1 |
| otros_diureticos            |    1353 |   0.515152  |  0.499955 |     0 |     0 |     1 |   1   |     1 |
| clopidogrel                 |    1353 |   0.961567  |  0.192311 |     0 |     1 |     1 |   1   |     1 |

### Imputación 3

Nuevamente volvemos a solo considerar solo las características anteriores, pero esta vez, modificaremos los valores con los que rellenamos los datos de `ckmb`. Primero se hizo un análisis donde se probó que los valores medios dichos en [**1**] difieren de los cubanos, al menos registrados en el conjunto de datos que tenemos. Ahora bien, a pesar de los intentos por bscar valores estándar cubanos para rellenarpor defecto esta característica, recurrimos a rellenar con el promedio de esta según los datos que teníamos. Sin embargo, los datos que tenemos pueden presentar algún tipo de ruido, por las razones que vimos en un inicio con respecto a los distintos errores que tenía el conjunto de datos. Por lo tanto antes de utilizar algún valor de referencia se eliminaron datos aislados considereando el puntaje-z, es decir, se eliminaro los datos por encima o por debajo de las $3$ desviaciones estándar con respecto a la media. Y posterior a esto se agrupó en 2 conjuntos: los pacientes que padecieron algún infarto, y los que no; se calculó sus medias, y estas fueron usadas para rellenar los datos faltantes. Sus valores fueron $136.16$ y $112.19$ respectivamente.

A continuación los estadísticos del nuevo conjunto de datos:

|                             |   count |        mean |       std |   min |   25% |     50% |     75% |   max |
|:----------------------------|--------:|------------:|----------:|------:|------:|--------:|--------:|------:|
| estado_vital                |    1353 |   0.101996  |  0.302754 |     0 |     0 |   0     |   0     |     1 |
| edad                        |    1353 |  66.221     | 12.6557   |    13 |    57 |  67     |  75     |    98 |
| sexo                        |    1353 |   0.678492  |  0.467228 |     0 |     0 |   1     |   1     |     1 |
| peso                        |    1353 |  73.0266    | 11.9829   |    40 |    65 |  72     |  80     |   150 |
| hipertension_arterial       |    1353 |   0.849224  |  0.357963 |     0 |     1 |   1     |   1     |     1 |
| diabetes_mellitus           |    1353 |   0.2949    |  0.456167 |     0 |     0 |   0     |   1     |     1 |
| tabaquismo                  |    1353 |   0.478197  |  0.499709 |     0 |     0 |   0     |   1     |     1 |
| frecuencia_cardiaca         |    1353 |  84.8537    | 14.9467   |    30 |    78 |  86     |  88     |   180 |
| presion_arterial_sistolica  |    1353 | 125.937     | 22.9879   |     0 |   120 | 130     | 130     |   240 |
| presion_arterial_diastolica |    1353 |  74.7007    | 14.0609   |     0 |    70 |  70     |  80     |   130 |
| hb                          |    1353 | 127.725     | 25.9975   |     8 |   126 | 133     | 135     |   238 |
| creatinina                  |    1353 | 103.455     | 59.4396   |    38 |    78 |  89     | 113     |  1036 |
| ckmb                        |    1353 | 139.97      | 87.8473   |     0 |   107 | 136.159 | 136.159 |   960 |
| fibrilacion_auricular       |    1353 |   0.0155211 |  0.123659 |     0 |     0 |   0     |   0     |     1 |
| insuficiencia_renal_cronica |    1353 |   0.0325203 |  0.177443 |     0 |     0 |   0     |   0     |     1 |
| ieca                        |    1353 |   0.872136  |  0.334062 |     0 |     1 |   1     |   1     |     1 |
| furosemida                  |    1353 |   0.182557  |  0.386446 |     0 |     0 |   0     |   0     |     1 |
| otros_diureticos            |    1353 |   0.515152  |  0.499955 |     0 |     0 |   1     |   1     |     1 |
| clopidogrel                 |    1353 |   0.961567  |  0.192311 |     0 |     1 |   1     |   1     |     1 |

### Consideración IMPORTANTE con la Imputación de datos

Hay varias de las características escogidas que son categóricas y tienen exactamente dos posibles valores como es el `tabaquismo`. De estas características en [**1,2,3**] se expresa el por ciento que representa cada categoría como promedio, sin embargo esta media en términos reales está entre $0$ y $1$ y carece de sentido, por lo que de imputar los valores faltantes de estos con dicho valor, no fue una opción acertada por el equipo de trabajo. Luego se pensó en rellenar los valores faltantes tomando en cuenta una distribución de Bernuilli con probabilidad igual a cada media, lo cual estadísticamente nos debía mantener la proporción correctamente, mientras que los datos tendría solamente los dos posibles valores. Sin embarg esto tenía un inconveniente: al rellenar de forma aleatoria CON sentido, no dejaba de ser aleatorio el clasificar un paciente con una categoría que no le tocara, lo cual podía empeorar aún más los datos. Por lo tanto decimos no involucrar variasbles categóricas en esto.

## Aumentado de Datos

Otra forma para mejorar el conjunto de datos era aumentando estos, con datos ficticios pero con sentido. Para esto lo que hicimos fue perturbar algunas características particulares para cada registro. Es decir, se iba seleccionando de manera aleatoria registros de pacientes al que íbamos a mutar; y luego pertubábamos los valores de algunas de las características que consideramos perturbar. Note que de esta forma evitamos repetir datos, y aumentamos estos, sin afectar notablemente las estadísticas del conjunto. Es importante señalar que esta técnica nos permite además equilibrar las clases, en la medida que querramos. Y por último aclarar que las mutaciones realizadas son alterando con una distribución uniforme centrada en el valor real teniendo en cuenta un pequeño margen al rededor de este valor. No obsatante hay casos donde el margen alrededor de un valor puede producir un valor mayor que el máximo permitido o menor que el mínimo permitido, y para esto se tienen en cuenta estos extremos, limitando la generación de un valor fuerade estos límites.

## Aumentado 1

En este caso se consideró aumentar el conjunto de datos **Imputados 1**, introduciendo ruido en las siguientes características:

| Característica                | Radio del Ruido | Mínimo | Máximo |
|:------------------------------|:---------------:|:------:|:------:|
| "edad"                        | 3               | 0      |   -    |
| "peso"                        | 5               | 0      |   -    |
| "frecuencia_cardiaca"         | 4               | -      |   -    |
| "presion_arterial_sistolica"  | 10              | 60     |   -    |
| "presion_arterial_diastolica" | 10              | 30     |   -    |
| "hb"                          | 3               | 1      |   -    |
| "creatinina"                  | 3               | -      |   -    |
| "ckmb"                        | 5               | 1      |   -    |

El análisis estadístico del nuevo conjunto conformado se muestra a continuación:

|                             |   count |        mean |       std |      min |      25% |      50% |      75% |       max |
|:----------------------------|--------:|------------:|----------:|---------:|---------:|---------:|---------:|----------:|
| estado_vital                |    2353 |   0.483638  |  0.499838 |  0       |   0      |   0      |   1      |    1      |
| edad                        |    2353 |  69.9107    | 12.3854   | 13       |  62      |  71      |  79      |   98.7568 |
| sexo                        |    2353 |   0.652359  |  0.476323 |  0       |   0      |   1      |   1      |    1      |
| peso                        |    2353 |  72.3787    | 12.8671   | 36.7444  |  64.2311 |  70      |  81.8933 |  150      |
| hipertension_arterial       |    2353 |   0.892478  |  0.309842 |  0       |   1      |   1      |   1      |    1      |
| diabetes_mellitus           |    2353 |   0.40374   |  0.490751 |  0       |   0      |   0      |   1      |    1      |
| tabaquismo                  |    2353 |   0.442839  |  0.496827 |  0       |   0      |   0      |   1      |    1      |
| frecuencia_cardiaca         |    2353 |  86.6645    | 19.5607   | 27.4616  |  78      |  86.6146 |  92      |  180      |
| presion_arterial_sistolica  |    2353 | 118.537     | 26.9504   |  0       | 110      | 120      | 130      |  240      |
| presion_arterial_diastolica |    2353 |  70.7748    | 16.1871   |  0       |  66.1173 |  70      |  79.5733 |  130      |
| hb                          |    2353 | 127.979     | 23.6837   |  5.28708 | 126      | 132      | 135.493  |  238      |
| creatinina                  |    2353 | 113.769     | 61.3651   | 38       |  84.2816 | 101.464  | 129      | 1036      |
| ckmb                        |    2353 | 157.708     | 83.8851   |  0       | 110      | 180.505  | 184.7    |  960      |
| fibrilacion_auricular       |    2353 |   0.0123247 |  0.110354 |  0       |   0      |   0      |   0      |    1      |
| insuficiencia_renal_cronica |    2353 |   0.0467488 |  0.211145 |  0       |   0      |   0      |   0      |    1      |
| ieca                        |    2353 |   0.796005  |  0.403051 |  0       |   1      |   1      |   1      |    1      |
| furosemida                  |    2353 |   0.282618  |  0.450368 |  0       |   0      |   0      |   1      |    1      |
| otros_diureticos            |    2353 |   0.446239  |  0.497207 |  0       |   0      |   0      |   1      |    1      |
| clopidogrel                 |    2353 |   0.955801  |  0.20558  |  0       |   1      |   1      |   1      |    1      |

## Aumentado 2

En este caso tomamos como conjunto base para aumentar los datos **Imputados 2**, introduciendo el mismo ruido anterior. Y obtuvimos los siguietes estadísticos:

|                             |   count |        mean |       std |     min |      25% |      50% |      75% |       max |
|:----------------------------|--------:|------------:|----------:|--------:|---------:|---------:|---------:|----------:|
| estado_vital                |    2353 |   0.483638  |  0.499838 |  0      |   0      |   0      |   1      |    1      |
| edad                        |    2353 |  69.9488    | 12.1616   | 13      |  62      |  71      |  78.9094 |   98.6706 |
| sexo                        |    2353 |   0.644284  |  0.478831 |  0      |   0      |   1      |   1      |    1      |
| peso                        |    2353 |  71.7893    | 12.7119   | 35.7687 |  64      |  70      |  80      |  150      |
| hipertension_arterial       |    2353 |   0.883553  |  0.320828 |  0      |   1      |   1      |   1      |    1      |
| diabetes_mellitus           |    2353 |   0.401615  |  0.490329 |  0      |   0      |   0      |   1      |    1      |
| tabaquismo                  |    2353 |   0.439014  |  0.496372 |  0      |   0      |   0      |   1      |    1      |
| frecuencia_cardiaca         |    2353 |  87.0026    | 19.1238   | 27.8326 |  79      |  86.5472 |  92      |  180      |
| presion_arterial_sistolica  |    2353 | 119.012     | 26.5931   |  0      | 110      | 120      | 130      |  240      |
| presion_arterial_diastolica |    2353 |  70.9426    | 16.2095   |  0      |  66.7629 |  70      |  79.5006 |  130      |
| hb                          |    2353 | 128.141     | 23.6933   |  6.2508 | 124.457  | 132.714  | 135.938  |  238      |
| creatinina                  |    2353 | 115.12      | 61.4779   | 38      |  84.5848 | 104      | 131.837  | 1036      |
| ckmb                        |    2353 | 158.444     | 86.2776   |  0      | 110      | 180.884  | 184.7    |  960      |
| fibrilacion_auricular       |    2353 |   0.0174246 |  0.130875 |  0      |   0      |   0      |   0      |    1      |
| insuficiencia_renal_cronica |    2353 |   0.0556736 |  0.229339 |  0      |   0      |   0      |   0      |    1      |
| ieca                        |    2353 |   0.78283   |  0.412407 |  0      |   1      |   1      |   1      |    1      |
| furosemida                  |    2353 |   0.297918  |  0.45744  |  0      |   0      |   0      |   1      |    1      |
| otros_diureticos            |    2353 |   0.448789  |  0.497476 |  0      |   0      |   0      |   1      |    1      |
| clopidogrel                 |    2353 |   0.958776  |  0.19885  |  0      |   1      |   1      |   1      |    1      |

## Aumentado 3

En esta ocasión aumentamos los datos **Imputados 3**, introduciendo el mismo ruido que el explicado en **Aumentado 1**. Y obtuvimos los siguietes estadísticos:

|                             |   count |        mean |       std |      min |      25% |      50% |      75% |   max |
|:----------------------------|--------:|------------:|----------:|---------:|---------:|---------:|---------:|------:|
| estado_vital                |    2353 |   0.483638  |  0.499838 |  0       |   0      |   0      |   1      |     1 |
| edad                        |    2353 |  70.1336    | 12.3336   | 13       |  62      |  71.4926 |  79      |    98 |
| sexo                        |    2353 |   0.644284  |  0.478831 |  0       |   0      |   1      |   1      |     1 |
| peso                        |    2353 |  71.7276    | 13.0378   | 35.0936  |  63.3737 |  70      |  80.3142 |   150 |
| hipertension_arterial       |    2353 |   0.888228  |  0.315153 |  0       |   1      |   1      |   1      |     1 |
| diabetes_mellitus           |    2353 |   0.401615  |  0.490329 |  0       |   0      |   0      |   1      |     1 |
| tabaquismo                  |    2353 |   0.436039  |  0.495998 |  0       |   0      |   0      |   1      |     1 |
| frecuencia_cardiaca         |    2353 |  86.8292    | 19.5003   | 26.0446  |  78      |  86.8357 |  92.1336 |   180 |
| presion_arterial_sistolica  |    2353 | 118.868     | 26.7385   |  0       | 110      | 120      | 130      |   240 |
| presion_arterial_diastolica |    2353 |  70.8226    | 16.037    |  0       |  66.1415 |  70      |  79.5434 |   130 |
| hb                          |    2353 | 128.176     | 23.6413   |  5.52494 | 125      | 132.653  | 135.963  |   238 |
| creatinina                  |    2353 | 114.94      | 63.4081   | 38       |  84.2657 | 102      | 130.211  |  1036 |
| ckmb                        |    2353 | 142.841     | 81.5202   |  0       | 112.576  | 136.159  | 140.879  |   960 |
| fibrilacion_auricular       |    2353 |   0.0127497 |  0.112216 |  0       |   0      |   0      |   0      |     1 |
| insuficiencia_renal_cronica |    2353 |   0.0526987 |  0.223479 |  0       |   0      |   0      |   0      |     1 |
| ieca                        |    2353 |   0.78878   |  0.408261 |  0       |   1      |   1      |   1      |     1 |
| furosemida                  |    2353 |   0.292393  |  0.454958 |  0       |   0      |   0      |   1      |     1 |
| otros_diureticos            |    2353 |   0.447089  |  0.497298 |  0       |   0      |   0      |   1      |     1 |
| clopidogrel                 |    2353 |   0.960051  |  0.195881 |  0       |   1      |   1      |   1      |     1 |

## Aumentado 4

Ahora cambiamos tanto de conjunto como de vector de características. Consideramos el **Vector de Características 2** y los datos sin valores faltantes del conjunto de datos original. Y luego introducimos el siguiente ruido:

| Característica                | Radio del Ruido | Mínimo | Máximo |
|:------------------------------|:---------------:|:------:|:------:|
| "edad"                        | 3               | 0      |   -    |
| "peso"                        | 5               | 0      |   -    |
| "frecuencia_cardiaca"         | 4               | -      |   -    |
| "presion_arterial_sistolica"  | 10              | 60     |   -    |
| "presion_arterial_diastolica" | 10              | 30     |   -    |
| "hb"                          | 3               | 1      |   -    |
| "creatinina"                  | 3               | -      |   -    |
| "ckmb"                        | 5               | 1      |   -    |
| "trigliceridos"               | 1.5             | 0      | 9      |
| "glicemia"                    | 3               | 3.3    | 43     |
| "colesterol"                  | 1               | 1.1    | 10     |
| "escala_grace"                | 5               | 34     | 190    |

Y una vez hecho este el análisis estadístico de los nuevos dato arrojó:

|                             |   count |      mean |         std |      min |       25% |       50% |      75% |      max |
|:----------------------------|--------:|----------:|------------:|---------:|----------:|----------:|---------:|---------:|
| estado_vital                |    2000 |   0.5     |   0.500125  |  0       |   0       |   0.5     |   1      |    1     |
| edad                        |    2000 |  70.4026  |  12.4734    | 11.9322  |  62.5635  |  71.7273  |  79.5298 |   98     |
| sexo                        |    2000 |   0.6765  |   0.467929  |  0       |   0       |   1       |   1      |    1     |
| peso                        |    2000 |  72.9861  |  13.2575    | 35.4206  |  64.2904  |  71.5067  |  83.5488 |  114.984 |
| hipertension_arterial       |    2000 |   0.8985  |   0.302065  |  0       |   1       |   1       |   1      |    1     |
| diabetes_mellitus           |    2000 |   0.4445  |   0.497034  |  0       |   0       |   0       |   1      |    1     |
| tabaquismo                  |    2000 |   0.41    |   0.491956  |  0       |   0       |   0       |   1      |    1     |
| frecuencia_cardiaca         |    2000 |  86.3318  |  18.5097    | 28.1017  |  80.5024  |  87       |  92      |  156.429 |
| presion_arterial_sistolica  |    2000 | 117.429   |  27.1183    | 50       | 105       | 120       | 130      |  243.077 |
| presion_arterial_diastolica |    2000 |  69.9066  |  17.02      | 20       |  63.0855  |  70       |  78.1978 |  120     |
| hb                          |    2000 | 125.813   |  22.1363    |  6.95634 | 126.065   | 132.15    | 134.413  |  238     |
| creatinina                  |    2000 | 117.269   |  61.2573    | 38       |  86       | 106.563   | 133.77   | 1036     |
| ckmb                        |    2000 | 153.894   | 105.814     |  1       |  96       | 137.169   | 179.388  |  960     |
| fibrilacion_auricular       |    2000 |   0.023   |   0.149941  |  0       |   0       |   0       |   0      |    1     |
| insuficiencia_renal_cronica |    2000 |   0.037   |   0.188809  |  0       |   0       |   0       |   0      |    1     |
| ieca                        |    2000 |   0.779   |   0.415024  |  0       |   1       |   1       |   1      |    1     |
| furosemida                  |    2000 |   0.32    |   0.466593  |  0       |   0       |   0       |   1      |    1     |
| otros_diureticos            |    2000 |   0.623   |   0.484756  |  0       |   0       |   1       |   1      |    1     |
| clopidogrel                 |    2000 |   0.954   |   0.209537  |  0       |   1       |   1       |   1      |    1     |
| trigliceridos               |    2000 |   1.39495 |   0.842557  |  0       |   0.8     |   1.2642  |   1.9    |    9     |
| glicemia                    |    2000 |   8.67511 |   3.85318   |  3.3     |   5.93859 |   7.50324 |  10.5741 |   43     |
| colesterol                  |    2000 |   4.91998 |   1.04105   |  1.34003 |   4.22137 |   4.9     |   5.6    |   10     |
| escala_grace                |    2000 | 122.813   |  27.8104    | 38.2071  | 106       | 125.604   | 143.81   |  190     |
| dialisis                    |    2000 |   0.004   |   0.0631347 |  0       |   0       |   0       |   0      |    1     |

## Aumentado 5

Y finalmente considerando el **Vector de Características 3** y el conjunto de datos original sin datos faltantes, se aumentó introducimos el siguiente ruido:

| Característica                | Radio del Ruido | Mínimo | Máximo |
|:------------------------------|:---------------:|:------:|:------:|
| "edad"                        | 3               | 0      |   -    |
| "peso"                        | 5               | 0      |   -    |
| "frecuencia_cardiaca"         | 4               | -      |   -    |
| "presion_arterial_sistolica"  | 10              | 60     |   -    |
| "presion_arterial_diastolica" | 10              | 30     |   -    |
| "hb"                          | 3               | 1      |   -    |
| "creatinina"                  | 3               | -      |   -    |
| "ckmb"                        | 5               | 1      |   -    |
| "trigliceridos"               | 1.5             | 0      | 9      |
| "glicemia"                    | 3               | 3.3    | 43     |
| "colesterol"                  | 1               | 1.1    | 10     |
| "escala_grace"                | 5               | 34     | 190    |
| "tiempo_isquemia"             | 10              | 0      | 2880   |

Y obtuvimos las siguientes estadísticas:

|                                   |   count |       mean |         std |      min |        25% |       50% |       75% |      max |
|:----------------------------------|--------:|-----------:|------------:|---------:|-----------:|----------:|----------:|---------:|
| estado_vital                      |    1600 |   0.5      |   0.500156  |  0       |   0        |   0.5     |   1       |    1     |
| edad                              |    1600 |  70.211    |  12.3585    | 12.3572  |  62.3422   |  71       |  79.0125  |   98     |
| sexo                              |    1600 |   0.67375  |   0.468987  |  0       |   0        |   1       |   1       |    1     |
| peso                              |    1600 |  73.0336   |  13.5183    | 36.842   |  64.0549   |  71.7742  |  84.5261  |  114.932 |
| hipertension_arterial             |    1600 |   0.903125 |   0.29588   |  0       |   1        |   1       |   1       |    1     |
| diabetes_mellitus                 |    1600 |   0.456875 |   0.498293  |  0       |   0        |   0       |   1       |    1     |
| tabaquismo                        |    1600 |   0.396875 |   0.489403  |  0       |   0        |   0       |   1       |    1     |
| frecuencia_cardiaca               |    1600 |  85.7737   |  18.6717    | 29.2064  |  80        |  86.4424  |  91.4677  |  153     |
| presion_arterial_sistolica        |    1600 | 117.912    |  26.3188    | 50       | 105.796    | 120       | 130       |  240     |
| presion_arterial_diastolica       |    1600 |  70.7757   |  16.5994    | 20       |  63.363    |  70       |  79.2013  |  129.426 |
| hb                                |    1600 | 124.977    |  22.968     |  6.88853 | 125.739    | 132       | 134       |  145     |
| creatinina                        |    1600 | 116.073    |  56.7261    | 36.1943  |  86        | 108       | 134.189   | 1036     |
| ckmb                              |    1600 | 151.731    | 106.398     |  1       |  92.8487   | 137.708   | 178.714   |  961     |
| fibrilacion_auricular             |    1600 |   0.034375 |   0.182247  |  0       |   0        |   0       |   0       |    1     |
| insuficiencia_renal_cronica       |    1600 |   0.02875  |   0.167155  |  0       |   0        |   0       |   0       |    1     |
| ieca                              |    1600 |   0.80625  |   0.395359  |  0       |   1        |   1       |   1       |    1     |
| furosemida                        |    1600 |   0.32875  |   0.469906  |  0       |   0        |   0       |   1       |    1     |
| otros_diureticos                  |    1600 |   0.604375 |   0.489137  |  0       |   0        |   1       |   1       |    1     |
| clopidogrel                       |    1600 |   0.96375  |   0.18697   |  0       |   1        |   1       |   1       |    1     |
| trigliceridos                     |    1600 |   1.42369  |   0.879115  |  0       |   0.863196 |   1.28673 |   1.87275 |    9     |
| glicemia                          |    1600 |   8.88566  |   4.08774   |  3.3     |   5.89875  |   7.54824 |  10.9706  |   27.3   |
| colesterol                        |    1600 |   4.95931  |   1.06753   |  1.63765 |   4.25627  |   4.9535  |   5.64193 |   10     |
| escala_grace                      |    1600 | 122.102    |  27.6048    | 42       | 106        | 123.799   | 143.012   |  190     |
| dialisis                          |    1600 |   0.0025   |   0.0499531 |  0       |   0        |   0       |   0       |    1     |
| tiempo_isquemia                   |    1600 | 322.212    | 278.08      |  0       | 150        | 210       | 360       | 2880     |
| scacest                           |    1600 |   0.82375  |   0.381152  |  0       |   1        |   1       |   1       |    1     |
| insuficiencia_cardiaca_congestiva |    1600 |   0.024375 |   0.154259  |  0       |   0        |   0       |   0       |    1     |
| enfermedad_arterias_coronarias    |    1600 |   0.45875  |   0.498451  |  0       |   0        |   0       |   1       |    1     |
| infarto_miocardio_agudo           |    1600 |   0.091875 |   0.28894   |  0       |   0        |   0       |   0       |    1     |

### Consideraciones IMPORTANTES con el Aumento de Datos

Es necesario destacar 2 cosas. La primera es que se incrementó por lo general solo los datos de los pacientes muertos ya uqe era la más desbalanceada. Sin embargo hay casos donde ambos clases fueron incrementadas por la escacez de datos. Y por último de suma importancia es que al introducir datos nuevos y ficticios NO podíamos testear nuestros algoritmos con estos datos; solamente podíamos entrenarlos.

# Bibliografía

[**1**] Risk markers by sex for in-hospital mortality in patients with acute coronary syndrome: A machine learning approach. Blanca Vázquez, Gibran Fuentes-Pineda, Fabian García, Gabriela Borrayo, Juan Prohías.

[**2**] Temas de Medicina Interna. Roca Goderich, María Elena Noya Chaveco, Noel Lorenzo Moya González. 5.ed.   Editorial Ciencias Médicas. 2017.

[**3**] Tratado de Medicina Interna. Travessera de Gracia, 17-2. 08021 Barcelona, España. 2012.
            """)
