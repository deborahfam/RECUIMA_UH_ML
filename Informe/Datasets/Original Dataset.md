# Características del Dataset original

## Falta de balance en los datos

El _dataset_ mostró una clara falta de balance en los datos teniendo en cuenta el _feature_ objetivo, la cantidad de pacientes que no fallecen, luego de ingresar al hospital, es mucho mayor de los que sí lo hacen, en la muestra observada. Como se puede apreciar en la siguiente imagen:

![[Pasted image 20230621032020.png]]

## Correlación entre características:

En el _dataset_ original existen características que están estrechamente correlacionadas con otras, lo que significa que la información que brindan es redundante. Por lo tanto dichas características pueden ser eliminadas del _dataset_ para aligerar el peso del mismo sin sacrificar veracidad de los datos.

![[Pasted image 20230621032522.png]]
Como se observa en la imagen anterior lo que se eliminó fue:
- escala GRACE
- presión arterial diastólica

Producto de la falta de datos no se pudo realizar el PCA en el _dataset_ original. 
![[Pasted image 20230621041927.png]]
Como se muestra en la imagen anterior existen datos demasiado dispersos para poder realizar esta prueba en el _dataset_, dado que el PCA no admite falta de datos. También por la ocurrencia de datos binarios y no binarios se necesita normalizar los datos para llevarlos a una métrica estándar.
Por otra parte se tomó medidas para reajustar el _dataset_ quitando los _features_ en los que faltaban datos. Como resultado de esta operación se obtuvo el [[Feature Reduction]].