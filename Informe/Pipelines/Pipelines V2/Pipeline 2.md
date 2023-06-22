# Primera forma de balance de pesos

Utilizando un parámetro adicional donde indicamos weight = "balanced" en el modelo de Regresión Logística y otros que lo permiten, con esto el algoritmo se encargará de equilibrar la clase minoritaria durante el entrenamiento.

## Logistic Regression

![[Pasted image 20230621054704.png]]

```
                precision    recall  f1-score   support

           0       0.97      0.72      0.82       239
           1       0.28      0.81      0.41        32

    accuracy                           0.73       271
   macro avg       0.62      0.76      0.62       271
weighted avg       0.88      0.73      0.77       271
```

## SVM

![[Pasted image 20230621060250.png]]

```
              precision    recall  f1-score   support

           0       0.96      0.74      0.83       239
           1       0.28      0.75      0.40        32

    accuracy                           0.74       271
   macro avg       0.62      0.74      0.62       271
weighted avg       0.88      0.74      0.78       271
```

## Random Forest

![[Pasted image 20230621060818.png]]

```
              precision    recall  f1-score   support

           0       0.90      0.98      0.94       239
           1       0.55      0.19      0.28        32

    accuracy                           0.89       271
   macro avg       0.72      0.58      0.61       271
weighted avg       0.86      0.89      0.86       271
```

# Subsampling en la clase mayoritaria

Se realiza esto para disminuir la cantidad de elemento en la clase mayoritaria e intentar balancear de otra forma el _dataset_.

## Logistic Regression

![[Pasted image 20230621055026.png]]

```
				precision    recall  f1-score   support

           0       0.93      0.34      0.50       239
           1       0.14      0.81      0.24        32

    accuracy                           0.40       271
   macro avg       0.54      0.58      0.37       271
weighted avg       0.84      0.40      0.47       271
```

## SVM

![[Pasted image 20230621060340.png]]

```
              precision    recall  f1-score   support

           0       0.83      0.14      0.24       239
           1       0.11      0.78      0.19        32

    accuracy                           0.22       271
   macro avg       0.47      0.46      0.22       271
weighted avg       0.74      0.22      0.24       271
```

## Random Forest

![[Pasted image 20230621060928.png]]

```
              precision    recall  f1-score   support

           0       0.98      0.36      0.52       239
           1       0.16      0.94      0.28        32

    accuracy                           0.42       271
   macro avg       0.57      0.65      0.40       271
weighted avg       0.88      0.42      0.49       271
```

# Oversampling en la clase minoritaria

Con esto se aumentan los datos en la clase minoritaria en otro intento por balancear el _dataset_.

## Logistic Regression

![[Pasted image 20230621055355.png]]

```
              precision    recall  f1-score   support

           0       0.96      0.86      0.91       239
           1       0.40      0.72      0.52        32

    accuracy                           0.84       271
   macro avg       0.68      0.79      0.71       271
weighted avg       0.89      0.84      0.86       271
```

## SVM

![[Pasted image 20230621060517.png]]

```
              precision    recall  f1-score   support

           0       0.96      0.73      0.83       239
           1       0.27      0.75      0.40        32

    accuracy                           0.73       271
   macro avg       0.61      0.74      0.61       271
weighted avg       0.88      0.73      0.78       271
```

## Random Forest

![[Pasted image 20230621061103.png]]

```
              precision    recall  f1-score   support

           0       0.92      0.97      0.95       239
           1       0.67      0.38      0.48        32

    accuracy                           0.90       271
   macro avg       0.79      0.67      0.71       271
weighted avg       0.89      0.90      0.89       271
```

# Resampling con SMOTE + Tomek

Ahora probaremos una técnica ampliamente utilizada que consiste en aplicar simultáneamente un algoritmo de submuestreo y un algoritmo de sobremuestreo al conjunto de datos al mismo tiempo. En este caso, usaremos SMOTE para el sobremuestreo: encuentre puntos vecinos cercanos y agregue puntos "en línea recta" entre ellos. Y usaremos Tomek para el submuestreo que elimina los de diferentes clases que son vecinos más cercanos y nos permite ver mejor el límite de decisión (la zona límite de nuestras clases).

## Logistic Regression

![[Pasted image 20230621055650.png]]

```
              precision    recall  f1-score   support

           0       0.95      0.85      0.90       239
           1       0.38      0.69      0.49        32

    accuracy                           0.83       271
   macro avg       0.67      0.77      0.69       271
weighted avg       0.89      0.83      0.85       271
```

## SVM

![[Pasted image 20230621060700.png]]

```
              precision    recall  f1-score   support

           0       0.95      0.74      0.83       239
           1       0.27      0.72      0.39        32

    accuracy                           0.74       271
   macro avg       0.61      0.73      0.61       271
weighted avg       0.87      0.74      0.78       271
```

## Random Forest

![[Pasted image 20230621061313.png]]

```
              precision    recall  f1-score   support

           0       0.93      0.96      0.94       239
           1       0.58      0.44      0.50        32

    accuracy                           0.90       271
   macro avg       0.76      0.70      0.72       271
weighted avg       0.89      0.90      0.89       271
```

# Ensamble de modelos

Otra forma de intentar balancear las clases del _dataset_.

## Balanced Bagging

![[Pasted image 20230621060129.png]]

```
              precision    recall  f1-score   support

           0       0.96      0.80      0.87       239
           1       0.33      0.75      0.46        32

    accuracy                           0.79       271
   macro avg       0.65      0.77      0.67       271
weighted avg       0.89      0.79      0.82       271
```

