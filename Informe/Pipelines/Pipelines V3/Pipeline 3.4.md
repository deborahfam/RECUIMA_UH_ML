# Preliminares

## K-Fold
![[Pasted image 20230622115044.png]]

## Stratified K-Fold
![[Pasted image 20230622115135.png]]

## Stratified Group K-Fold
![[Pasted image 20230622115156.png]]

## Group K-Fold
![[Pasted image 20230622115216.png]]

## Times Series Split
![[Pasted image 20230622115242.png]]

# Modelos y evaluación

## SVM

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.5780
======= Fold 1 ========
El AUC en el conjunto de validación es 0.7765
======= Fold 2 ========
El AUC en el conjunto de validación es 0.7223
======= Fold 3 ========
El AUC en el conjunto de validación es 0.7517
======= Fold 4 ========
El AUC en el conjunto de validación es 0.6720
El resultado AUC promediado es 0.7001
```

## Gradient Boosting

```
(1256, 63)
======= Fold 0 ========
El AUC en el conjunto de validación es 0.8576
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9396
======= Fold 2 ========
El AUC en el conjunto de validación es 0.8023
======= Fold 3 ========
El AUC en el conjunto de validación es 0.8085
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9411
El resultado AUC promediado es 0.8698
```

## Hist Gradient Boosting

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.8967
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9537
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9230
======= Fold 3 ========
El AUC en el conjunto de validación es 0.8949
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9643
El resultado AUC promediado es 0.9265
```

## SNN

```
Epoch 1/50
23/23 [==============================] - 1s 7ms/step - loss: 0.5105 - accuracy: 0.8331 - val_loss: 0.3296 - val_accuracy: 0.9055
Epoch 2/50
23/23 [==============================] - 0s 2ms/step - loss: 0.2847 - accuracy: 0.9128 - val_loss: 0.2240 - val_accuracy: 0.9055
Epoch 3/50
23/23 [==============================] - 0s 2ms/step - loss: 0.2145 - accuracy: 0.9153 - val_loss: 0.1891 - val_accuracy: 0.9204
```

![[Pasted image 20230622120723.png]]

![[Pasted image 20230622120727.png]]