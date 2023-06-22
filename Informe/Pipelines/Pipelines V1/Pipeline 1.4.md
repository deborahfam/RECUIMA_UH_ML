# Preliminares

## Balance

![[Pasted image 20230622100233.png]]

## Correlación
![[Pasted image 20230622100956.png]]

## Esparcimiento
![[Pasted image 20230622101027.png]]

## Distribución
![[Pasted image 20230622101117.png]]

# Modelos y evaluación

## SVM

![[Pasted image 20230622101236.png]]

```
              precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       1.00      0.36      0.53        22

    accuracy                           0.94       252
   macro avg       0.97      0.68      0.75       252
weighted avg       0.95      0.94      0.93       252
```

## Random Forest

![[Pasted image 20230622101343.png]]

```
              precision    recall  f1-score   support

         0.0       0.93      0.98      0.96       230
         1.0       0.60      0.27      0.37        22

    accuracy                           0.92       252
   macro avg       0.77      0.63      0.67       252
weighted avg       0.90      0.92      0.91       252
```

## Logistic Regression

![[Pasted image 20230622101446.png]]

```
              precision    recall  f1-score   support

         0.0       0.95      0.98      0.97       232
         1.0       0.64      0.45      0.53        20

    accuracy                           0.94       252
   macro avg       0.80      0.71      0.75       252
weighted avg       0.93      0.94      0.93       252
```

# K-Fold Cross Validation

## SVM

![[Pasted image 20230622101602.png]]

```
              precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       1.00      0.36      0.53        22

    accuracy                           0.94       252
   macro avg       0.97      0.68      0.75       252
weighted avg       0.95      0.94      0.93       252
```

## Gaussian Naive Bayes

![[Pasted image 20230622101656.png]]

```
              precision    recall  f1-score   support

         0.0       1.00      0.33      0.50       230
         1.0       0.12      1.00      0.22        22

    accuracy                           0.39       252
   macro avg       0.56      0.67      0.36       252
weighted avg       0.92      0.39      0.47       252
```

## MLP

![[Pasted image 20230622101743.png]]

```
              precision    recall  f1-score   support

         0.0       0.95      0.94      0.95       230
         1.0       0.44      0.50      0.47        22

    accuracy                           0.90       252
   macro avg       0.70      0.72      0.71       252
weighted avg       0.91      0.90      0.90       252
```

## KNN

![[Pasted image 20230622101818.png]]

```
              precision    recall  f1-score   support

         0.0       0.95      0.97      0.96       230
         1.0       0.62      0.45      0.53        22

    accuracy                           0.93       252
   macro avg       0.79      0.71      0.74       252
weighted avg       0.92      0.93      0.92       252
```

## Random Forest

![[Pasted image 20230622101947.png]]

```
              precision    recall  f1-score   support

         0.0       0.95      0.99      0.97       230
         1.0       0.83      0.45      0.59        22

    accuracy                           0.94       252
   macro avg       0.89      0.72      0.78       252
weighted avg       0.94      0.94      0.94       252
```

## Logistic Regression

![[Pasted image 20230622102022.png]]

```
              precision    recall  f1-score   support

         0.0       0.95      0.97      0.96       230
         1.0       0.62      0.45      0.53        22

    accuracy                           0.93       252
   macro avg       0.79      0.71      0.74       252
weighted avg       0.92      0.93      0.92       252
```