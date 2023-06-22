# Preliminares

A partir de una descripción estadística inicial del conjunto de datos, inferimos que algunas características de los datos son binarias u ordinales, mientras que otras características son continuas. Además, los valores mínimos y máximos para algunas características, especialmente para la presión arterial sistólica, no son realistas. Esto sugiere la presencia de valores atípicos en los datos.

Este pipeline se ejecuta utilizando el [[Feature Reduction]] y se le aplica la técnica de aumento de datos.

![[Pasted image 20230622054543.png]]

![[Pasted image 20230622054605.png]]

Como se observa en este _dataset_ luego de realizadas las modificaciones la tabla de correlaciones sugiere que no existe dependencia entre _features_. Por tanto se procedió a la ejecución de los modelos con su uso.

# Modelos y evaluación

## SVM

![[Pasted image 20230622054926.png]]

```
              precision    recall  f1-score   support

         0.0       0.78      0.77      0.78       235
         1.0       0.78      0.78      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Logistic Regression

![[Pasted image 20230622055152.png]]

```
              precision    recall  f1-score   support

         0.0       0.80      0.81      0.81       262
         1.0       0.76      0.75      0.75       209

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## # K-Fold Cross Validation

![[Pasted image 20230622055252.png]]

```
              precision    recall  f1-score   support

         0.0       0.78      0.77      0.78       235
         1.0       0.78      0.78      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Gaussian Naive Bayes

![[Pasted image 20230622055410.png]]

```
              precision    recall  f1-score   support

         0.0       0.74      0.76      0.75       235
         1.0       0.75      0.74      0.75       236

    accuracy                           0.75       471
   macro avg       0.75      0.75      0.75       471
weighted avg       0.75      0.75      0.75       471
```

## MLP

![[Pasted image 20230622055450.png]]

```
              precision    recall  f1-score   support

         0.0       0.93      0.83      0.88       235
         1.0       0.85      0.94      0.89       236

    accuracy                           0.89       471
   macro avg       0.89      0.89      0.89       471
weighted avg       0.89      0.89      0.89       471
```

## KNN

![[Pasted image 20230622055530.png]]

```
              precision    recall  f1-score   support

         0.0       0.86      0.75      0.80       235
         1.0       0.78      0.87      0.82       236

    accuracy                           0.81       471
   macro avg       0.82      0.81      0.81       471
weighted avg       0.82      0.81      0.81       471
```

## Random Forest

![[Pasted image 20230622055942.png]]

```
             precision    recall  f1-score   support

         0.0       0.97      0.93      0.95       235
         1.0       0.93      0.97      0.95       236

    accuracy                           0.95       471
   macro avg       0.95      0.95      0.95       471
weighted avg       0.95      0.95      0.95       471
```