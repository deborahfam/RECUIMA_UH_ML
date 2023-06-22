# Preliminares

En este pipeline se trabaja con [[Improved Dataset]], además también se aplica el balance de pesos y la técnica para aumento de datos.

# Modelos y evaluación

## Balanced Weights

### Logistic Regression

![[Pasted image 20230622063743.png]]

```
              precision    recall  f1-score   support

         0.0       0.72      0.74      0.73       235
         1.0       0.74      0.72      0.73       236

    accuracy                           0.73       471
   macro avg       0.73      0.73      0.73       471
weighted avg       0.73      0.73      0.73       471
```

### SVM

![[Pasted image 20230622064137.png]]

```
              precision    recall  f1-score   support

         0.0       0.79      0.77      0.78       235
         1.0       0.77      0.80      0.79       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

### Random Forest

![[Pasted image 20230622102849.png]]

```
precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       0.89      0.36      0.52        22

    accuracy                           0.94       252
   macro avg       0.92      0.68      0.74       252
weighted avg       0.94      0.94      0.93       252
```

### Near Miss

![[Pasted image 20230622103117.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Subsampling

### Logistic Regression

![[Pasted image 20230622063922.png]]

```
              precision    recall  f1-score   support

         0.0       0.72      0.75      0.74       235
         1.0       0.74      0.71      0.72       236

    accuracy                           0.73       471
   macro avg       0.73      0.73      0.73       471
weighted avg       0.73      0.73      0.73       471
```

### SVM

![[Pasted image 20230622064040.png]]

```
              precision    recall  f1-score   support

         0.0       0.79      0.77      0.78       235
         1.0       0.78      0.79      0.79       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Ensamblado de modelos con Balanced Bagging

![[Pasted image 20230622064429.png]]

```
              precision    recall  f1-score   support

         0.0       0.94      0.89      0.91       235
         1.0       0.89      0.94      0.92       236

    accuracy                           0.92       471
   macro avg       0.92      0.92      0.91       471
weighted avg       0.92      0.92      0.91       471
```