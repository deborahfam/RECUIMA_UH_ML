# Modelos y evaluación

## Balanced Weights

### Logistic Regression

![[Pasted image 20230622105648.png]]

```
              precision    recall  f1-score   support

         0.0       0.99      0.85      0.91       230
         1.0       0.36      0.91      0.52        22

    accuracy                           0.85       252
   macro avg       0.68      0.88      0.72       252
weighted avg       0.94      0.85      0.88       252
```

### SVM

![[Pasted image 20230622110343.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

## Random Forest

![[Pasted image 20230622110821.png]]

```
              precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       0.89      0.36      0.52        22

    accuracy                           0.94       252
   macro avg       0.92      0.68      0.74       252
weighted avg       0.94      0.94      0.93       252
```

## Subsampling

### Logistic Regression

![[Pasted image 20230622110047.png]]

```
              precision    recall  f1-score   support

         0.0       0.72      0.75      0.74       235
         1.0       0.74      0.71      0.72       236

    accuracy                           0.73       471
   macro avg       0.73      0.73      0.73       471
weighted avg       0.73      0.73      0.73       471
```

### SVM

![[Pasted image 20230622110723.png]]

```
              precision    recall  f1-score   support

         0.0       0.79      0.77      0.78       235
         1.0       0.78      0.79      0.79       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Random Forest

![[Pasted image 20230622110932.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Conjunto de modelos con Balanced Bagging

![[Pasted image 20230622110200.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```


