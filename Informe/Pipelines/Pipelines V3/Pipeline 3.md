# Técnicas para dividir el dataset en Train y Test

## K-Fold
![[Pasted image 20230621231602.png]]

## Stratified K-Fold
![[Pasted image 20230621231645.png]]

## Stratified Group K-Fold
![[Pasted image 20230621231854.png]]

## Group K-Fold
![[Pasted image 20230621231919.png]]

## Time Series Split
![[Pasted image 20230621232005.png]]

# Algoritmos empleados en la etapa

## SVM

```
Precision: 0.7778 
Recall: 0.8819 
Accuracy: 0.8819 
AUC: 0.7407
```

## Hist Gradient Boosting y Gradient Boosting

```
======= Fold 0 ======== 
El AUC en el conjunto de validación es 0.9583 
Precision: 0.9790 
Recall: 0.9485 

======= Fold 1 ======== 
El AUC en el conjunto de validación es 0.9583 
Precision: 0.9790 
Recall: 0.9485 

======= Fold 2 ======== 
El AUC en el conjunto de validación es 0.6199 
Precision: 0.7020 
Recall: 0.5157 

======= Fold 3 ======== 
El AUC en el conjunto de validación es 0.7344 
Precision: 0.8169 
Recall: 0.8372 

======= Fold 4 ======== 
El AUC en el conjunto de validación es 0.8849 
Precision: 0.9470 
Recall: 0.9504 


El resultado AUC promediado es 0.8312 
Precision promediado es 0.8848 
Recall promediado es 0.8400 (1353, 25)

...
Hist Gradient Boosting

El resultado AUC promediado es 0.8487 
Precision promediado es 0.9159 
Recall promediado es 0.9258
```

## SVC

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9583
Precision: 0.9898
Recall: 0.9897

======= Fold 1 ========
El AUC en el conjunto de validación es 0.9583
Precision: 0.9898
Recall: 0.9897

======= Fold 2 ========
El AUC en el conjunto de validación es 0.6748
Precision: 0.8248
Recall: 0.7736

======= Fold 3 ========
El AUC en el conjunto de validación es 0.6967
Precision: 0.8786
Recall: 0.8586

======= Fold 4 ========
El AUC en el conjunto de validación es 0.7635
Precision: 0.9700
Recall: 0.9690


El resultado AUC promediado es 0.8103
Precision promediado es 0.9306
Recall promediado es 0.9161
```

