# Support Vector Classifier (SVC)

![[Pasted image 20230621044400.png]]

```
				precision recall f1-score support 
			0   0.96      0.74   0.83     239 
			1   0.28      0.75   0.40     32 
	
accuracy                         0.74     271 
macro avg       0.62      0.74   0.62     271 
weighted avg    0.88      0.74   0.78     271
```

```
 precision    recall  f1-score   support

           0       0.97      0.72      0.82       239
           1       0.28      0.81      0.41        32

    accuracy                           0.73       271
   macro avg       0.62      0.76      0.62       271
weighted avg       0.88      0.73      0.77       271
```
# Random Forest

![[Pasted image 20230621044528.png]]

```
				precision recall f1-score support 
			0   0.91      0.98   0.95     239 
			1   0.69      0.28   0.40     32 
	
accuracy                         0.90     271 
macro avg       0.80      0.63   0.67     271 
weighted avg    0.89      0.90   0.88     271
```

# Logistic Regression

![[Pasted image 20230621045137.png]]

```
				precision recall f1-score support 
			0   0.91      0.98   0.94     236 
			1   0.71      0.34   0.46     35
			 
accuracy                         0.90     271 
macro avg       0.81      0.66   0.70     271 
weighted avg    0.88      0.90   0.88     271
```

# Ten-Fold Cross Validation

Se utilizó con el fin de agrupar los datos en grupos de 10. Luego de esto se corrieron nuevamente algunos modelos.

# Support Vector Machine (SVM)

![[Pasted image 20230621045611.png]]

```
				precision recall f1-score support 
			0   0.88      1.00   0.94     239 
			1   0.00      0.00   0.00     32
			 
accuracy                         0.88     271 
macro avg       0.44      0.50   0.47     271 
weighted avg    0.78      0.88   0.83     271
```

# Gaussian Naive Bayes

![[Pasted image 20230621050723.png]]

```
				precision recall f1-score support 
			0   0.93      0.85   0.89     239 
			1   0.33      0.53   0.40     32 
			
accuracy                         0.82     271 
macro avg       0.63      0.69   0.65     271 
weighted avg    0.86      0.82   0.83     271
```

# MLP

![[Pasted image 20230621051343.png]]

```
				precision recall f1-score support 
			0   0.91      0.90   0.91     239 
			1   0.33      0.38   0.35     32 
				
accuracy                         0.84     271 
macro avg       0.62      0.64   0.63     271 
weighted avg    0.85      0.84   0.84     271
```

# KNN

![[Pasted image 20230621051621.png]]

```
				precision recall f1-score support 
			0   0.90      0.94   0.92     239 
			1   0.30      0.19   0.23     32 
			
accuracy                         0.85     271 
macro avg       0.60      0.56   0.57     271 
weighted avg    0.83      0.85   0.84     271
```