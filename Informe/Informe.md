# Seminario de Machine Learning

## Aprendizaje Automático orientado a la detección de factores de riesgo para pacientes de infarto

## Autores:

### Josué Rodríguez Ramírez C412
### Mauro José Bolado Vizoso C411
### Gabriel Hernández Rodríguez C411
### Lázaro Daniel González Martínez C411
### Deborah Famadas Rodríguez C412
### Belsai Arango Hernández C411

##  I - Estado del arte

El uso de machine learning en la medicina, especialmente en el campo de las afecciones cardíacas, ha experimentado un gran avance en los últimos años. Gracias al progreso en las técnicas de aprendizaje automático y al aumento en la capacidad computacional, se han abierto nuevas oportunidades de investigación en la modelización cardiovascular. Sus aplicaciones en afecciones cardíacas abarcan desde la predicción y diagnóstico de enfermedades hasta la personalización de tratamientos y la identificación de factores de riesgo. Algunas de las técnicas más utilizadas en este campo incluyen redes neuronales artificiales (ANN), redes neuronales convolucionales (CNN), máquinas de vectores de soporte (SVM), árboles de decisión, bosques aleatorios y deep learning. El uso de este recurso en el diagnóstico y tratamiento de afecciones cardíacas permite a los médicos y profesionales de la salud tomar decisiones informadas y mejorar la atención al paciente.

### I.1 - Distintas estrategias usadas comunmente

#### I.1.1 - Redes neuronales artificiales (ANN)
Las ANN son una de las técnicas más comunes utilizadas en la predicción de enfermedades cardíacas. Estos modelos pueden manejar datos no lineales y son capaces de aprender de los errores a través de un proceso de retropropagación.
Redes neuronales convolucionales (CNN): Las CNN son una subcategoría de las redes neuronales que se utilizan comúnmente en el análisis de imágenes médicas. En el contexto de las enfermedades cardíacas, las CNN pueden ser utilizadas para analizar imágenes de electrocardiogramas (ECG) y ecocardiogramas para detectar signos de enfermedad cardíaca.

#### I.1.2 - Máquinas de vectores de soporte (SVM)
Las SVM son otra técnica comúnmente utilizada en la predicción de enfermedades cardíacas. Estos modelos son capaces de manejar datos de alta dimensión y pueden ser eficaces en la identificación de patrones complejos.

#### I.1.3 - Árboles de decisión y bosques aleatorios
Estos modelos son útiles para identificar las características más importantes en la predicción de enfermedades cardíacas. Los bosques aleatorios, en particular, son eficaces para manejar datos de alta dimensión y pueden proporcionar una medida de la importancia de las características.

#### I.1.4 - Deep Learning
El Deep Learning es una subcategoría del aprendizaje automático que utiliza redes neuronales con muchas capas (deep neural networks). Estos modelos son capaces de aprender características de alto nivel a partir de los datos y han demostrado ser eficaces en la predicción de enfermedades cardíacas.

### I.2 - Actualidad

#### Estudio de García-Ordás et al. (2023)
Publicado en la revista Multimedia Tools and Applications utilizó ANN para predecir la enfermedad cardíaca con una precisión del 83.5%.
    
#### "Machine learning prediction of mortality in Acute Myocardial Infarction." - Oliveira M, Seringa J, Pinto FJ, Henriques R, Magalhães T. (2023).
Este estudio creó un modelo basado en aprendizaje automático para el análisis predictivo de la mortalidad en pacientes con infarto agudo de miocardio a la admisión, utilizando diferentes variables para analizar su impacto en los modelos predictivos.

#### "Prognostic Value of Machine-Learning-Based PRAISE Score for Ischemic and Bleeding Events in Patients With Acute Coronary Syndrome Undergoing Percutaneous Coronary Intervention." (2023). 
Este estudio presenta el PRAISE (Prediction of Adverse Events Following an Acute Coronary Syndrome) score, un modelo basado en aprendizaje automático para predecir la muerte por cualquier causa, infarto de miocardio y sangrado en el primer año en pacientes con síndrome coronario agudo.

#### "A Machine Learning-Based Applied Prediction Model for Identification of Acute Coronary Syndrome (ACS) Outcomes and Mortality in Patients during the Hospital Stay." (2023). 
Este estudio utilizó el conjunto de datos del Registro de Infarto Agudo de Miocardio de Corea (KAMIR-NIH), que contiene datos de 13,104 pacientes con 551 características. El rendimiento del modelo de aprendizaje automático fue comparado con otros modelos aplicados.

#### "Identification of Coronary Culprit Lesion in ST Elevation Myocardial Infarction by Using Deep Learning." (2023). 
Este estudio utilizó un modelo de aprendizaje profundo con una red neuronal convolucional para identificar la lesión culpable en pacientes con infarto de miocardio con elevación del segmento ST (STEMI).

#### "Comparison of conventional scoring systems to machine learning models for the prediction of major adverse cardiovascular events in patients undergoing coronary computed tomography angiography." (2022).
Este estudio compara el rendimiento pronóstico de los sistemas de puntuación convencionales con un modelo de aprendizaje automático en la tomografía computarizada de coronarias para discriminar entre los pacientes con y sin eventos cardiovasculares adversos mayores.


## 1 - Introducción

### 1.1 - Objetivos del trabajo y descripción del problema
El proyecto tiene como objetivo principal lograr clasificar, de la mejor manera posibles, a los pacientes infartados que ingresan en hospitales en dos clases, aquellos que tienen riesgo de muerte y los que son de riesgo menor. Para ello, a lo largo de este trabajo, se estará utilizando un conjunto de datos proporcionado por un grupo de hospitales cubanos.
Cabe mencionar que los datos proporcionados no presentaban el mejor estado de consistencia, causado por la falta de valores en muchas características presentes en el _dataset_, de donde el primer problema clave a solucionar era construir un _dataset_ que fuera consistente y permitiera entrenar los modelos necesarios para obtener los resultados deseados.
Objetivamente la única necesidad del proyecto no era esta y como tal otro de sus objetivos también es proporcionar a los usuarios finales, ya sean los doctores, enfermeros u otro personal capacitado para atender a los pacientes con el problema en cuestión, la capacidad de saber que exámenes, análisis y datos son más fiables al momento de tomar una decisión de esta índole.
Para lograr esto a lo largo del trabajo se expondrán las razones de cuales características de los datos conservar, cuales pueden ser catalogadas como irrelevantes e incluso cuales son datos redundantes. Por supuesto se trabajará con las técnicas necesarias para lograr que no haya pérdida de información de los datos originales y obtener un buen rsultado.

### 1.2 - Marco teórico

#### 1.2.1 - Descripción de algunas características (features)

##### Infarto Miocardio Agudo:
El **infarto agudo de miocardio** («agudo» significa "súbito", _mio_ "músculo" y _cardio_ "corazón"), frecuentemente abreviado como **IAM** o **IMA**, y conocido en el lenguaje coloquial como **ataque cardiaco** o **infarto** es un evento médico muy grave que refleja la muerte de células cardíacas provocada por la isquemia resultante del desequilibrio entre la demanda y el aporte de riego sanguíneo por la circulación coronaria.

##### Fibrilación Auricular:
La **fibrilación auricular** (FA) es la arritmia cardiaca más frecuente en la práctica clínica con una prevalencia del 1% en la población general.  La FA es una enfermedad que se caracteriza por latidos auriculares descoordinados y desorganizados, produciendo un ritmo cardíaco rápido e irregular (es decir, latidos cardiacos irregulares).

##### VAM:
**Ventilación Artifical Mecánica**, se emplea un aparato mecanico para ayudar o sustituir la funcion respiratoria en pacientes portadores de insuficiencia respiratoria de cualquier causa.

##### Escala ASA: 
El propósito de la **escala ASA** es categorizar, y posteriormente comunicar el riesgo del paciente de someterse a cualquier procedimiento que requiera anestesia, permitiendo valorar su estado fisiológico, enfermedades sistémicas (por ejemplo, diabetes no controlada) y estados agregados del paciente.

##### Betabloqueadores:
Los betabloqueadores, también conocidos como agentes bloqueantes beta adrenérgicos, **son medicamentos que reducen la presión arterial**. Los betabloqueantes funcionan como bloqueadores de los efectos de la hormona epinefrina, también conocida como "adrenalina".

##### Clopidogrel:
El **clopidogrel** es un agente antiplaquetario (del tipo tienopiridina) administrado por vía oral, que inhibe la formación de coágulos en la enfermedad arterial coronaria, enfermedad vascular periférica, y enfermedad cerebrovascular.

##### Heparina:
La **heparina** es un glicosaminoglicano muy sulfatado que se utiliza ampliamente como anticoagulante inyectable, y tiene la densidad de carga más alta conocida de todas las biomoléculas.

##### Estatinas:
Las **estatinas** son inhibidores de la 3-hidroxi-3-metilglutaril-coenzima A reductasa (HMG-CoA reductasa). Esta enzima cataliza un paso esencial de la vía del mevalonato, la conversión de la HMG-CoA a mevalonato, que es un metabolito clave en la en la biosíntesis de colesterol.

##### Estreptoquinasa:
La **estreptoquinasa** es una enzima extracelular producida por el estreptococo beta hemolítico, usado como medicamento efectivo y económico que disuelve coagulos sanguíneos, indicado en algunos casos de infarto de miocardio y embolismo pulmonar.

##### Reperfusión:
En cardiología, el **fenómeno de no reflujo** es la falta de sangre disponible para reperfundir un área isquémica después de que la obstrucción física haya sido anulada y se relaciona con la falta de recuperación funcional de la zona dañada. Por lo general se asocia luego de la reperfusión con la terapia trombolítica, en la angioplastia transluminal coronaria (ATC) primaria y durante otras intervenciones coronarias. Puede estar asociado con daño microvascular.

##### Coronariografía
Este procedimiento se llama **coronariografía**. Permite medir las presiones por delante y por detrás de las válvulas cardíacas, así como detectar reflujo de sangre a través de las mismas. Es decir, que permite el diagnóstico preciso de valvulopatías.

##### GRACE:
La escala GRACE permite estimar el pronóstico y mortalidad de una persona con infarto agudo de miocardio y se evalúan las siguientes variables: Edad, Presión arterial sistólica y Frecuencia cardiaca.

##### Furosemida:
La **furosemida** es un diurético de asa utilizado para reducir la retención de líquidos que puede producirse en la insuficiencia cardíaca congestiva, hipertensión arterial , la insuficiencia hepática y edemas.

##### IECA:
Los inhibidores de la enzima convertidora de angiotensina (IECA) son medicamentos utilizados para el tratamiento de la hipertensión arterial. Bloquean a distinto nivel el sistema renina-angiotensina, un mecanismo que tiene el organismo para regular de forma precisa la presión arterial.

##### Trombolisis:
**Trombólisis** es el procedimiento que se utiliza para disolver un coágulo sanguíneo (trombo) que se ha formado dentro de una arteria o una vena.

##### AVC:
El **accidente cerebrovascular embólico** es que el que se produce como consecuencia de que un émbolo o fragmento de un coágulo sanguíneo que vino desde el corazón obstruye el flujo de sangre al cerebro.

##### Aminas:
Las **aminas** simpaticomiméticas son una clase de drogas cuyas propiedades mimetizan (son agonistas adrenérgicos) las de la hormona adrenalina.

##### Electrocardiograma:
El electrocardiograma (ECG o EKG, a partir del alemán Elektrokardiogramm) es la representación visual de la actividad eléctrica del corazón en función del tiempo, que se obtiene, desde la superficie corporal, en el pecho, con un electrocardiógrafo en forma de cinta continua.

##### SCA:
El **síndrome coronario agudo** (**SCA**) hace referencia al grupo de síntomas atribuidos a la obstrucción de las arterias coronarias. El síntoma más común que indica el diagnóstico de un SCA es el dolor de pecho, generalmente irradiado hacia el brazo izquierdo o el ángulo de la mandíbula, de tipo opresivo, y asociado a náuseas. El síndrome coronario agudo generalmente ocurre como resultado de uno de tres problemas: infarto agudo de miocardio con ST elevado (30%), infarto agudo de miocardio sin ST elevado (25%), o angina inestable (38%). Aunque el SCA es usualmente asociado con trombosis coronaria, también puede ser asociado con el uso de cocaína "Cocaína"​ El dolor cardíaco en el pecho también puede ser causado por anemia, bradicardia (frecuencia cardiaca o taquicardia (frecuencia cardiaca excesivamente rápida).

##### Segmento ST:
El **segmento ST** representa el período isoeléctrico cuando los ventrículos se encuentran entre la [despolarización](https://es.wikipedia.org/wiki/Despolarizaci%C3%B3n "Despolarización") y la [repolarización](https://es.wikipedia.org/wiki/Hiperpolarizaci%C3%B3n "Hiperpolarización").

##### Presión Arterial Sistólica:
La **presión arterial sistólica** (la primera cifra) es la presión sanguínea en las arterias durante la sístole ventricular, cuando la sangre es expulsada desde el corazón a las arterias. 

##### Presión Arterial Diastólica:
La **presión arterial diastólica** (el número inferior) es la presión en la diástole, cuando el corazón se relaja y la presión arterial cae.

##### Índice Killip:
La **clasificación Killip-Kimball** es una estratificación individual basada en la evidencia de los pacientes con infarto agudo de miocardio, que permite establecer un pronóstico de la evolución de la afección, y las probabilidades de muerte en los 30 primeros días tras el infarto.

##### Hiperlipoproteinemia:
La **hiperlipidemia, hiperlipidosis o hiperlipemia** (literalmente: lípidos elevados de la sangre) consiste en la presencia de niveles elevados de los lípidos en la sangre. No puede considerarse una patología sino un desajuste metabólico que puede ser secundario a muchas enfermedades y puede contribuir a muchas formas de enfermedad, especialmente cardiovasculares. Está estrechamente vinculado a los términos **hipercolesterolemia** (los niveles elevados de colesterol) e **hiperlipoproteinemia** (los niveles elevados de lipoproteínas).

##### CABG:
**El baipás de arteria coronaria sin circulación extra-corpórea** o cirugía de "corazón latiente" es una forma de cirugía de injerto de derivación de arteria coronaria (CABG, por sus siglas en inglés) que se realiza sin baipás cardiopulmonar (máquina de circulación extracorpórea) como tratamiento para la enfermedad de las arterias coronarias.

##### Filtración Glomerular:
La **tasa o índice de filtración glomerular** (**TFG**, **IFG** o **GFR** por sus siglas en inglés: _Glomerular Filtration Rate_) es el volumen de fluido filtrado por unidad de tiempo desde los capilares glomerulares renales hacia el interior de la cápsula de Bowman.

Teniendo en cuenta estas definiciones se esclarece un poco la lectura del documento y es posible la comprensión de las decisiones tomadas a lo largo del desarrollo del trabajo.

## 2 - Desarrollo

Véase [[Original Dataset]] para tener todos los detalles necesarios acerca de los datos originales.
Dados los problemas anteriormente mencionados se modificó el conjunto de datos (_dataset_) para que fuera posible el uso de los mismos en el proyecto. Inicialmente se redujo la cantidad de características (_features_) a 17 con el objetivo de eliminar columnas muy dispersas y con información redundante. Véase [[Feature Reduction]].
Con esta reducción en los datos originales y con el completamiento de los datos faltantes se procedió a realizar un nuevo _dataset_. Una vez confeccionado el [[Improved Dataset]] se inició el desarrollo de la primera fase de predicción [[Pipeline 1]], esta fase se usaron distintos algoritmos, que luego se repetirán en cada uno de los cambios al _dataset_, para comparar con las versiones anteriores y manteniendo una comparación entre los distintos algoritmos, para así optimizar tanto el modelo a emplear como los datos a utilizar.

### 2.1 - Algoritmos utilizados en el proyecto

#### 2.1.1 - Logistic regression
La regresión logística es una técnica de análisis de datos que utiliza las matemáticas para encontrar las relaciones entre dos factores de datos. Luego, utiliza esta relación para predecir el valor de uno de esos factores basándose en el otro. Normalmente, la predicción tiene un número finito de resultados, como un sí o un no (caso binario).
Los modelos de regresión logística son matemáticamente menos complejos que otros métodos de ML. Por lo tanto, puede implementarlos incluso si nadie de su equipo tiene una profunda experiencia en ML. Pueden procesar grandes volúmenes de datos a alta velocidad porque requieren menos capacidad computacional, como memoria y potencia de procesamiento. Esto los hace ideales para que las organizaciones que están empezando con proyectos de ML obtengan ganancias rápidas (o estudiantes que aún no trabajan).
Se puede usar para encontrar respuestas a preguntas que tienen dos o más resultados finitos. También puede usarlo para preprocesar datos. Por ejemplo, puede ordenar los datos con un amplio rango de valores en un rango de valores más pequeño y finito. A continuación, puede procesar este conjunto de datos más pequeño mediante el uso de otras técnicas de ML para obtener un análisis más preciso.

#### 2.1.2 - Support Vector Machine
**SVM** funciona correlacionando datos a un espacio de características de grandes dimensiones de forma que los puntos de datos se puedan categorizar, incluso si los datos no se puedan separar linealmente de otro modo.
Se destaca por ser efectivo en espacios de alta dimensionalidad, aun cuando el número de dimensiones supera el número de muestras y una eficiente gestión de la memoria, al usar solo un subconjunto de puntos en la función de decisión.

#### 2.1.3 - Random forest
Hay principalmente cuatro sectores en los que se utiliza principalmente Random Forest.
El sector bancario utiliza principalmente este algoritmo para la identificación del riesgo de préstamo. Con su uso, en la medicina, se pueden identificar las tendencias y los riesgos de las enfermedades. Se pueden identificar las áreas de uso similar de la tierra mediante este. Las tendencias de marketing se pueden identificar utilizándolo.
**Random Forest** es capaz de realizar tareas de clasificación y regresión. Es capaz de manejar grandes conjuntos de datos con alta dimensionalidad. Mejora la precisión del modelo y evita el problema de sobreajuste.

#### 2.1.4 - Multi Layer Perceptron
El **perceptrón multicapa** es una red neuronal artificial (RNA) formada por múltiples capas, de tal manera que tiene capacidad para resolver problemas que no son linealmente separables, lo cual es la principal limitación del perceptrón (también llamado perceptrón simple). El perceptrón multicapa puede estar totalmente o localmente conectado. En el primer caso cada salida de una neurona de la capa "i" es entrada de todas las neuronas de la capa "i+1", mientras que en el segundo cada neurona de la capa "i" es entrada de una serie de neuronas (región) de la capa "i+1".

#### 2.1.5 - Gaussian Naive Bayes
Naive Bayes es un algoritmo de aprendizaje automático probabilístico que se utiliza para muchas funciones de clasificación y se basa en el teorema de Bayes. Gaussian Naive Bayes es la extensión de naive Bayes. Si bien se utilizan otras funciones para estimar la distribución de datos, la distribución gaussiana o normal es la más sencilla de implementar, ya que necesitará calcular la media y la desviación estándar de los datos de entrenamiento.
¿Cómo calcular las probabilidades cuando X es una variable continua? Si asumimos que X sigue una distribución particular, puede usar la función de densidad de probabilidad de esa distribución para calcular la probabilidad de probabilidades.
Si asumimos que las X siguen una distribución gaussiana o normal, debemos sustituir la densidad de probabilidad de la distribución normal y llamarla bayesiana ingenua gaussiana. Para calcular esta fórmula, necesita la media y la varianza de X.

![](https://d14b9ctw0m6fid.cloudfront.net/ugblog/wp-content/uploads/2021/02/C3.png)

En la fórmula anterior, sigma y mu es la varianza y la media de la variable continua X calculada para una clase dada c de Y.

#### 2.1.6 - Support Vector Classifier
El objetivo de un **SVC lineal** (Support Vector Classifier) es adecuarse a los datos que se proporcionan, devolviendo un hiperplano “ideal” que divide o categoriza sus datos. Desde allí, después de obtener el hiperplano, es posible entonces alimentar algunas características al clasificador para ver lo que es la clase “predecida”.

#### 2.1.7 - K-Nearest Neighbors
El algoritmo KNN es el más simple y también un algoritmo de aprendizaje automático muy práctico. También puede manejar problemas de clasificación y, naturalmente, puede manejar problemas de clasificación múltiple, como la clasificación del iris. Sencillo, fácil de entender y muy potente al mismo tiempo. También puede manejar problemas de regresión, es decir, predicción.

#### 2.1.8 - Sequential Neural Network
Un modelo Sequential es apropiado para una _pila_ de capas, donde cada capa tiene exactamente un tensor de entrada y un tensor de salida.

#### 2.1.9 - Gradient Boosting
_**Gradient boosting**_ o **Potenciación del gradiente,** es una técnica de aprendizaje automático utilizado para el análisis de la regresión y para problemas de clasificación estadística, el cual produce un modelo predictivo en forma de un conjunto de modelos de predicción débiles, típicamente árboles de decisión. Construye el modelo de forma escalonada como lo hacen otros métodos de boosting, y los generaliza permitiendo la optimización arbitraria de una función de pérdida diferenciable.

#### 2.1.10 - Hist Gradient Boosting
Este estimador es mucho más rápido que GradientBoostingClassifier para grandes conjuntos de datos (n_samples >= 10 000).
Este estimador tiene soporte nativo para valores faltantes (NaN). Durante el entrenamiento, el cultivador de árboles aprende en cada punto de división si las muestras con valores faltantes deben ir al hijo izquierdo o derecho, según la ganancia potencial. Al predecir, las muestras con valores faltantes se asignan al hijo izquierdo o derecho en consecuencia. Si no se encontraron valores faltantes para una característica determinada durante el entrenamiento, las muestras con valores faltantes se asignan al hijo que tenga la mayor cantidad de muestras.

### 2.2 - ¿Por qué estos modelos?

|#| Machine Learning Article | Methods used | Dataset |  
|-| ---------------------------------| --------------------| --------------------------------|
|1| [ECG-based machine-learning algorithms for heartbeat classification](https://www.nature.com/articles/s41598-021-97118-5#Sec18)            |  Two-event related moving-averages (TERMA), Fractional-Fourier-transform (FrFT) algorithms, SVM, Artificial-neural-network (ANN)      | Shaoxing People’s Hospital (SPH) database, which consists of more than 10,000 patients           | 80%        | Precisión en la predicción
|2| [Artificial intelligence and machine learning in cardiovascular computed tomography](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8554359/)             | Decision trees, ensembles, logistic regression and deep neural networks with transparency     | Extracting Global Clinical Metadata from Large Patient DatabaSEs (ECLIPSE)           |
|3| [Detecting cardiac pathologies via machine learning on heart-rate variability time series and related markers](https://www.nature.com/articles/s41598-020-64083-4.pdf)             |Feed-forward neural networks, Clustering reciprocities and cliques, Classificaction tasks via algorithmic network theory      | Data collected from 24h Hoter recording over a sample of 2829 labelled patients          | 85% |
|4| [Automatic Prediction of Cardiovascular and Cerebrovascular Events Using Heart Rate Variability Analysis](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0118504&type=printable)             |Support vector machine, tree-based classifier, artificial neural network| Database of 139 Holter recordings with clinical data of hypertensive patients followed up for at least 12 months| 71.4% - 87.8% |
|5| [Prediction of cardiovascular risk factors from retinal fundus photographs via deep learning](https://www.nature.com/articles/s41551-018-0195-0)              | Deep Neural Network | using retinal fundus images from 48,101 patients from the UK Biobank and 236,234 patients from EyePACS |
|6| [Deep learning analysis of resting electrocardiograms for the detection of myocardial dysfunction, hypertrophy, and ischaemia: a systematic reviewt](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8482047/)              | regression tree, convolutional neural network(CNN), deep neural network(DNN), logistic regression, random forest, support vector machine (SVM)     | Six studies used DL ECG analysis to detect acute myocardial infarction and two to detect stable ischaemic heart disease, accuracy of 83–99.9%. The predictive accuracy of DL models was very high to detect both acute or stable forms of ischaemic heart disease, and furthermore, two studies demonstrated an accuracy of 99.81%14 and 99.72%15 to localize the territory of infarction. |
|7| [Use of Machine Learning Models to Predict Death After Acute Myocardial Infarction](https://jamanetwork.com/journals/jamacardiology/fullarticle/2777055) | Models based on extreme gradient descent boosting (XGBoost, an interpretable model), a neural network, and a meta-classifier model. | Chest Pain–MI Registry (CP-MI Registry; formerly known as the ACTION Registry) of the National Cardiovascular Data Registry (NCDR) |
|8| [Risk markers by sex for in-hospital mortality in patients with acute coronary syndrome: A machine learning approach](https://www.sciencedirect.com/science/article/pii/S2352914821002616) | Logistic Regression (LR), Support Vector Machines (SVM), Random Forest (RF), and eXtreme Gradient Boosting (XGB) |
|9| [Cardiovascular Disease Prediction by Machine Learning Algorithms Based on Cytokines in Kazakhs of China](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8200454/) | Decision Tree (DT), eXtreme Gradient Boosting (XGB), K-nearest neighbors (KNN), Logistic Regression (LR), Naive-Bayes, Random Forest (RF), Support Vector Machine (SVM)  |
|10| [Risk prediction of cardiovascular disease using machine learning classifiers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9206502/) | K-nearest neighbors (KNN), Multi-Layer Perceptron  |

### 2.3 - Pipelines

#### 2.3.1 - Pipeline 1
Por las características favorables a la solución del problema, por parte de cada uno de los algoritmos mencionados anteriormente y la popularidad de su uso que se puede apreciar en la tabla, se filtraron para ser utilizados en el [[Pipeline 1]] y ser sometidos a evaluación en nuestro problema. 

#### 2.3.2 - Pipeline 2
Luego de obtenidos los resultados de la primera predicción se procedió a realizar un balance de pesos y correr nuevamente los modelos. Esto se llevó a cabo en el [[Pipeline 2]].


#### 2.3.3 - Pipeline 3
Dado que estamos tratando con un conjunto de datos desequilibrado, se recomienda utilizar otras métricas en lugar de la precisión.
En este caso, proponemos utilizar AUC (*Area Under the Curve*), que es una medida de la capacidad del clasificador para distinguir entre clases y se utiliza como representación de la curva ROC. Cuanto mayor sea el AUC, mejor será el rendimiento del modelo para distinguir entre las clases positivas y negativas.
Una curva ROC (*curva característica operativa del receptor*) es un gráfico que muestra el rendimiento de un modelo de clasificación en todos los umbrales de clasificación. Esta curva traza dos parámetros: *Tasa de verdaderos positivos* (TPR) y *Tasa de falsos positivos* (FPR)
- TPR = TP / (TP + FN)
- FPR = FP / (FP + TN)
TPR frente a FPR se trazan en diferentes umbrales de clasificación. Reducir el umbral de clasificación clasifica más elementos como positivos, lo que aumenta tanto los falsos positivos como los verdaderos positivos. Con el objetivo de realizar este análisis se desarrolló el [[Pipeline 3]].


#### 2.3.4 - Nuevas Modificaciones a los dataset
Luego de todas las pruebas anteriormente realizadas y dados los resultados obtenidos en cada una de ellas, apreciando la progresión obtenida por los cambios se procedió a continuar modificando los datos. Estas modificaciones tienen como objetivo ajustar el _dataset_ para que sea más consistente y maniobrable con cada uno de los modelos.

Se procedió a aumentar el volumen de datos generando datos adicionales a partir de los datos reales ya presentes y con objetivo de balancear mejor las clases. Pero esta vez usando las técnicas de generación de datos que se ajustan al problema y claramente hacerlo de forma semi-automática, dado que la relación de características a tener en cuenta fue seleccionada por el equipo y no de forma aleatoria por algún algoritmo.

Para dar uso a otro grupo de características (_features_) se procedió a crear otro _dataset_ el cual tendría en lugar de 22 como el [[Improved Dataset]], otras 5 adicionales haciendo un total de 26 características. El objetivo de adicionar los nuevos _features_ era optimizar la toma de decisiones de cada uno de los modelos implementados, para más detales ver [[Final Dataset]].

#### 2.3.5 - Segunda ronda de pruebas
Luego de las modificaciones y la creación del nuevo _dataset_ se procedió a probar los modelos con cada uno de ellos para luego poder evaluar los resultados. Este proceso se dividió en tres pipelines:

- [[Pipeline 1.1]]
- [[Pipeline 2.1]]
- [[Pipeline 3.1]]

#### 2.3.6 - Tercera y Cuarta rondas de pruebas
La técnica de _Data Augmentation_ se estuvo perfeccionando, con el objetivo de que se ajustase lo más posible al problema y redujera el conflicto en el balance en los datos sin pérdida en la veracidad de los mismos.

Para probar estas modificaciones se llevó a cabo dos rondas más de de pruebas.

**Ronda 1**:
- [[Pipeline 1.2]]
- [[Pipeline 2.2]]
- [[Pipeline 3.2]]

**Ronda 2**:
- [[Pipeline 1.3]]
- [[Pipeline 2.3]]
- [[Pipeline 3.3]]

#### 2.3.7 - Completamiento de datos
Por último, con el objetivo de probar que el óptimo estaba en un punto medio, se probó completar todos los datos faltantes en el [[Original Dataset]], esto se realizó utilizando valores en algunos casos predeterminados, en otros se tomó la media e incluso otras heurísticas para poder rellenar los datos faltantes.

Terminado lo necesario se realizó la última ronda de pruebas:
- [[Pipeline 1.4]]
- [[Pipeline 2.4]]
- [[Pipeline 3.4]]

## 3 - Conclusiones
La carencia de algunas _features_ es un factor primordial en los resultados obtenidos, ejemplo de ello es la falta de un electrocardiograma, lo cual es recomendado en la mayoría de otras investigaciones semejantes en el tema. Incluso no es recomendable rellenar datos con valores ficticios, los resultados como se pudo apreciar, pueden ser no del todo satisfactorios en este caso.

Hay un [[Pipeline S]] donde se prueba con varias distribuciones de los datos, en el cual se muestran los únicos buenos resultados obtenidos de esta forma.

Luego de analizar cada uno de los dataset provistos con las distintas técnicas llegamos a la conclusión de que algunos modelos son mejores que otros, a continuación se presentará una selección de estos.

| Algoritmo             | Pipeline     | Acc  | Recall | Precisión | f1   |
|-----------------------|--------------|------|--------|-----------|------|
| SNN con SMOTE + Tomek |  [[Pipeline S]] | 0.85 | 0.74   | 0.96      | 0.91 |
| Balanced Bagging      | [[Pipeline 2.2]] | 0.87 | 0.77   | 0.98      | 0.93 |
| KNN                   | [[Pipeline 1.3]] | 0.91 | 0.98   | 0.86      | 0.90 |

De todos los mencionados anteriormente el más fiable es el que ocupa la primera posición de la tabla, pues se pudo probar con más datos y en distintas etapas de los _dataset_.

## 4 - Recomendaciones
 Se recomienda agregar más _features_ a los diferentes _dataset_, como antes se mencionó, con el objetivo de podar lo más posible la cantidad de _features_, sin perder veracidad.

Conseguir los valores de los _Electrocardiogramas_

Probar con otros _dataset_. ya sean nacionales o internacionales.

## PD: 
Disfrutar de la lectura de todo el informe y contactar a los creadores en caso de alguna otra recomendación.