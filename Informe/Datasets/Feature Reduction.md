Para un fácil manejo de la información, evitar la redundancia de los datos y eliminar todas aquellas características que se creían prescindibles en una primera instancia, el conjunto de datos original se redujo a una muestra de solo 17 características. 

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

Tras un poco de investi
## Estrategia de completado fijo:

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

Como resultado de esta operación se obtiene el [[Improved Dataset]].