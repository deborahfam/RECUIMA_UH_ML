# Preliminares

## Balance de los datos
![[Pasted image 20230622064724.png]]

## Correlación
![[Pasted image 20230622064806.png]]

## Distribución de los datos
![[Pasted image 20230622064838.png]]

# Modelos y evaluación:

## SVM

![[Pasted image 20230622065036.png]]

```
              precision    recall  f1-score   support

         0.0       0.83      0.80      0.81       235
         1.0       0.80      0.83      0.82       236

    accuracy                           0.82       471
   macro avg       0.82      0.82      0.82       471
weighted avg       0.82      0.82      0.82       471
```

## Logistic Regression

![[Pasted image 20230622065228.png]]

```
              precision    recall  f1-score   support

         0.0       0.79      0.84      0.82       262
         1.0       0.78      0.73      0.75       209

    accuracy                           0.79       471
   macro avg       0.79      0.78      0.79       471
weighted avg       0.79      0.79      0.79       471
```

## Random Forest

![[Pasted image 20230622065121.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.92      0.95       235
         1.0       0.92      0.98      0.95       236

    accuracy                           0.95       471
   macro avg       0.95      0.95      0.95       471
weighted avg       0.95      0.95      0.95       471
```

# K-Fold Cross Validation

## SVM

![[Pasted image 20230622065429.png]]

```
              precision    recall  f1-score   support

         0.0       0.83      0.80      0.81       235
         1.0       0.80      0.83      0.82       236

    accuracy                           0.82       471
   macro avg       0.82      0.82      0.82       471
weighted avg       0.82      0.82      0.82       471
```

## Gaussian Naive Bayes

![[Pasted image 20230622065536.png]]

```
              precision    recall  f1-score   support

         0.0       0.72      0.80      0.76       235
         1.0       0.78      0.69      0.73       236

    accuracy                           0.74       471
   macro avg       0.75      0.74      0.74       471
weighted avg       0.75      0.74      0.74       471
```

## MLP

![[Pasted image 20230622065615.png]]

```
              precision    recall  f1-score   support

         0.0       0.93      0.88      0.91       235
         1.0       0.89      0.94      0.91       236

    accuracy                           0.91       471
   macro avg       0.91      0.91      0.91       471
weighted avg       0.91      0.91      0.91       471
```

## KNN

![[Pasted image 20230622065756.png]]

```
Cross-validation score means:  0.7834219858156029
Accuracy:  0.9278131634819533
              precision    recall  f1-score   support

         0.0       1.00      0.86      0.92       235
         1.0       0.87      1.00      0.93       236

    accuracy                           0.93       471
   macro avg       0.94      0.93      0.93       471
weighted avg       0.94      0.93      0.93       471

```
