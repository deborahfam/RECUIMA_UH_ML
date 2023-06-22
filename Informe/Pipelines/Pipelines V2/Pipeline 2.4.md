# Modelos y evaluación

## Balanced Weights

### Logistic Regression

![[Pasted image 20230622114221.png]]

```
              precision    recall  f1-score   support

         0.0       0.99      0.85      0.91       230
         1.0       0.36      0.91      0.52        22

    accuracy                           0.85       252
   macro avg       0.68      0.88      0.72       252
weighted avg       0.94      0.85      0.88       252
```

### SVM

![[Pasted image 20230622114443.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

### Random Forest

![[Pasted image 20230622114616.png]]

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

![[Pasted image 20230622114302.png]]

```
              precision    recall  f1-score   support

         0.0       0.97      0.55      0.70       230
         1.0       0.15      0.82      0.25        22

    accuracy                           0.58       252
   macro avg       0.56      0.69      0.48       252
weighted avg       0.90      0.58      0.66       252
```

### SVM

![[Pasted image 20230622114539.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.56      0.71       230
         1.0       0.16      0.86      0.27        22

    accuracy                           0.58       252
   macro avg       0.57      0.71      0.49       252
weighted avg       0.91      0.58      0.67       252
```

### Random Forest\

![[Pasted image 20230622114704.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Conjunto de modelos con Balanced Bagging

![[Pasted image 20230622114401.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```

