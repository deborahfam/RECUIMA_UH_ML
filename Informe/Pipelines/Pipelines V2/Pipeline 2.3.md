# Modelos y evaluación

## Balanced Weights

### Logistic Regression

![[Pasted image 20230622111437.png]]

```
              precision    recall  f1-score   support

         0.0       0.99      0.85      0.91       230
         1.0       0.36      0.91      0.52        22

    accuracy                           0.85       252
   macro avg       0.68      0.88      0.72       252
weighted avg       0.94      0.85      0.88       252
```

### SVM

![[Pasted image 20230622111838.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

### Random Forest

![[Pasted image 20230622112009.png]]

```
              precision    recall  f1-score   support

         0.0       0.93      1.00      0.97       230
         1.0       1.00      0.27      0.43        22

    accuracy                           0.94       252
   macro avg       0.97      0.64      0.70       252
weighted avg       0.94      0.94      0.92       252
```

## Subsampling

### Logistic Regression

![[Pasted image 20230622111624.png]]

```
              precision    recall  f1-score   support

         0.0       0.97      0.55      0.70       230
         1.0       0.15      0.82      0.25        22

    accuracy                           0.58       252
   macro avg       0.56      0.69      0.48       252
weighted avg       0.90      0.58      0.66       252
```

### SVM

![[Pasted image 20230622111918.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.56      0.71       230
         1.0       0.16      0.86      0.27        22

    accuracy                           0.58       252
   macro avg       0.57      0.71      0.49       252
weighted avg       0.91      0.58      0.67       252
```

### Random Forest

![[Pasted image 20230622112158.png]]

```
              precision    recall  f1-score   support

         0.0       0.99      0.78      0.87       230
         1.0       0.29      0.91      0.43        22

    accuracy                           0.79       252
   macro avg       0.64      0.85      0.65       252
weighted avg       0.93      0.79      0.84       252
```

## Conjunto de modelos con Balanced Bagging

![[Pasted image 20230622111709.png]]

```
              precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```

## SNN

![[Pasted image 20230622113225.png]]

![[Pasted image 20230622113231.png]]

```
Epoch 1/20
76/76 [==============================] - 1s 3ms/step - loss: 0.5213 - accuracy: 0.7302 - val_loss: 0.4127 - val_accuracy: 0.8064
Epoch 2/20
76/76 [==============================] - 0s 2ms/step - loss: 0.3881 - accuracy: 0.8146 - val_loss: 0.3693 - val_accuracy: 0.8435
Epoch 3/20
76/76 [==============================] - 0s 1ms/step - loss: 0.3337 - accuracy: 0.8512 - val_loss: 0.3566 - val_accuracy: 0.8488
Epoch 4/20
76/76 [==============================] - 0s 1ms/step - loss: 0.3010 - accuracy: 0.8744 - val_loss: 0.3244 - val_accuracy: 0.8886
Epoch 5/20
76/76 [==============================] - 0s 1ms/step - loss: 0.2672 - accuracy: 0.8997 - val_loss: 0.3209 - val_accuracy: 0.8621
Epoch 6/20
76/76 [==============================] - 0s 1ms/step - loss: 0.2413 - accuracy: 0.9156 - val_loss: 0.3098 - val_accuracy: 0.8806
Epoch 7/20
76/76 [==============================] - 0s 1ms/step - loss: 0.2101 - accuracy: 0.9269 - val_loss: 0.2869 - val_accuracy: 0.8859
Epoch 8/20
76/76 [==============================] - 0s 1ms/step - loss: 0.1919 - accuracy: 0.9395 - val_loss: 0.2795 - val_accuracy: 0.8992
Epoch 9/20
76/76 [==============================] - 0s 1ms/step - loss: 0.1765 - accuracy: 0.9362 - val_loss: 0.2589 - val_accuracy: 0.8833
Epoch 10/20
```
