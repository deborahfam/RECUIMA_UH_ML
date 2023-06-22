# Resumen

Para la confección de este _dataset_ se utilizó como base el de [[Feature Reduction]]. El cambio consiste en reincorporarle otras 4 características del [[Original Dataset]] las cuales también se consideraron relevantes luego de una investigación un poco más exhaustiva. 
Por otra parte es en este _dataset_ donde se normalizan los datos y además se analiza la distribución probabilística para poder trabajar con los modelos que se tenían pensados.

![[Pasted image 20230621042935.png]]
La imagen anterior muestra la distribución de los datos, de los cuales como se aprecia existen varios que distribuyen normal lo cual justifica el uso del modelo de ML **Gaussian Naive Bayes**.
Este _dataset_ es el que se utilizó en el [[Pipeline 1]].

## Características agregadas

**Colesterol**:
Según busque en internet para confirmar, es uno de los principales factores de riesgo cardiovascular. Las personas que muestran un colesterol alto en sangre tienen el doble de posibilidades de sufrir un infarto miocardio.

**Diálisis**:
Hay relación directa entre las enfermedades renales crónicas (ERC) y las cardiovasculares (CV). Por un lado, la enfermedad CV es la causa fundamental de muerte en pacientes con ERC1. Por otro, tener ERC amplifica el riesgo de muerte en la enfermedad CV, se tenga otros factores de riesgo o no2. La ERC acelera la enfermedad CV, incluso antes de llegar a su grado de insuficiencia renal terminal (IRT) con necesidad de diálisis o trasplante.

**Trigliceridos**:
Cuando su cuerpo necesita energía, libera los triglicéridos. Sus partículas de lipoproteína de muy baja densidad llevan los triglicéridos a sus tejidos. Tener un alto nivel de triglicéridos puede aumentar el riesgo de enfermedades del corazón, como la enfermedad de las arterias coronarias.
Por tanto es un factor de riesgo importante en la causa del infarto.

**Glicemia**:
Tanto en hombres como en mujeres se observó que por cada 1% más de HbA1c aumentaba el riesgo de sufrir un infarto agudo de miocardio un 18%.