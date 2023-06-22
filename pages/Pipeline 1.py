import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )
image05 = 'picture/image05.png'
image06='picture/image06.png'
image07='picture/image07.png'
image08='picture/image08.png'
image09='picture/image09.png'
image10='picture/image10.png'
image11='picture/image11.png'
image12='picture/Pasted image 20230622054543.png'
image13='picture/Pasted image 20230622054605.png'
image14='picture/Pasted image 20230622054926.png'
image15='picture/Pasted image 20230622055152.png'
image16='picture/Pasted image 20230622055252.png'
image17='picture/Pasted image 20230622055410.png'
image18='picture/Pasted image 20230622055450.png'
image19='picture/Pasted image 20230622055530.png'
image20='picture/Pasted image 20230622055942.png'
image21='picture/Pasted image 20230622064724.png'
image22='picture/Pasted image 20230622064806.png'
image23='picture/Pasted image 20230622064838.png'
image24='picture/Pasted image 20230622065036.png'
image25='picture/Pasted image 20230622065228.png'
image26='picture/Pasted image 20230622065121.png'
image27='picture/Pasted image 20230622065429.png'
image28='picture/Pasted image 20230622065536.png'
image29='picture/Pasted image 20230622065615.png'
image30='picture/Pasted image 20230622065756.png'
image31='picture/Pasted image 20230622094758.png'
image32='picture/Pasted image 20230622094836.png'
image33='picture/Pasted image 20230622094902.png'
image34='picture/Pasted image 20230622094952.png'
image35='picture/Pasted image 20230622095112.png'
image36='picture/Pasted image 20230622095256.png'
image37='picture/Pasted image 20230622095153.png'
image38='picture/Pasted image 20230622095511.png'
image39='picture/Pasted image 20230622095632.png'
image40='picture/Pasted image 20230622095655.png'
image41='picture/Pasted image 20230622095756.png'
image42='picture/Pasted image 20230622095836.png'
image43='picture/Pasted image 20230622095953.png'
st.set_page_config(page_title="RECUIMA", layout="wide")

PAGES = {
    "Pipeline 1": "/Pipeline 1",
    "Pipeline 1.1": "/Pipeline 1.1",
    "Pipeline 1.2":"/Pipeline 1.2",
    "Pipeline 1.3":"/Pipeline 1.3",
    "Pipeline 1.4":"/Pipeline 1.4"
}
selection = st.sidebar.radio("", list(PAGES.keys()))

 # Create a function to display the selected page
def display_page(page):
    if page == "/Pipeline 1":
        st.sidebar.success("Pipeline 1")
        st.sidebar.write('SVM')
        st.sidebar.write('Random Forest')
        st.sidebar.write('Logistic Regression')
        st.sidebar.write('Gaussian Naive Bayes')
        st.sidebar.write('MLP')
        st.sidebar.write('KNN')
        st.markdown("""# Support Vector Classifier (SVC)
        
        """)
        st.image(image05, width=700)
        st.markdown("""
                    
        ```
        __________________precision recall   f1-score    support
                   0       0.97      0.72      0.82       239
                   1       0.28      0.81      0.41        32
        
            accuracy                           0.73       271
           macro avg       0.62      0.76      0.62       271
        weighted avg       0.88      0.73      0.77       271
        ```
        """)
        st.markdown("""# Random Forest""")
        
        st.image(image06, width=700)
        st.markdown("""
        ```
        ___________________________precision recall f1-score support 
        			0   0.91      0.98   0.95     239 
        			1   0.69      0.28   0.40     32 
        	
        accuracy                         0.90     271 
        macro avg       0.80      0.63   0.67     271 
        weighted avg    0.89      0.90   0.88     271
        ```
        """)
        st.markdown("""# Logistic Regression""")
        
        st.image(image07, width=700)
        st.markdown("""
        
        ```
        ___________________________precision recall f1-score support 
        			0   0.91      0.98   0.94     236 
        			1   0.71      0.34   0.46     35
        			 
        accuracy                         0.90     271 
        macro avg       0.81      0.66   0.70     271 
        weighted avg    0.88      0.90   0.88     271
        ```
        
        # 10-Fold Cross Validation
        
        Se utilizó con el fin de agrupar los datos en grupos de 10. Luego de esto se corrieron nuevamente algunos modelos.
        """)
        st.markdown("""# Support Vector Machine""")
        
        st.image(image08, width=700)
        st.markdown("""
        
        ```
        ___________________________precision recall f1-score support 
        			0   0.88      1.00   0.94     239 
        			1   0.00      0.00   0.00     32
        			 
        accuracy                         0.88     271 
        macro avg       0.44      0.50   0.47     271 
        weighted avg    0.78      0.88   0.83     271
        ```
        """)
        st.markdown("""# Gaussian Naive Bayes""")
        
        st.image(image09, width=700)
        st.markdown("""
        
        ```
        ____________________________precision recall f1-score support 
        			0   0.93      0.85   0.89     239 
        			1   0.33      0.53   0.40     32 
        			
        accuracy                         0.82     271 
        macro avg       0.63      0.69   0.65     271 
        weighted avg    0.86      0.82   0.83     271
        ```
        """)
        st.markdown("""# MLP""")
        
        st.image(image10, width=700)
        st.markdown("""
        
        ```
        __________________________precision recall f1-score support 
        			0   0.91      0.90   0.91     239 
        			1   0.33      0.38   0.35     32 
        				
        accuracy                         0.84     271 
        macro avg       0.62      0.64   0.63     271 
        weighted avg    0.85      0.84   0.84     271
        ```
        """)
        st.markdown("""# KNN""")
        
        st.image(image11, width=700)
        st.markdown("""
        
        ```
        ___________________________precision recall f1-score support 
        			0   0.90      0.94   0.92     239 
        			1   0.30      0.19   0.23     32 
        			
        accuracy                         0.85     271 
        macro avg       0.60      0.56   0.57     271 
        weighted avg    0.83      0.85   0.84     271""")
        
    if page == "/Pipeline 1.1":
        st.sidebar.success("Pipeline 1.1")
        st.sidebar.write('SVM')
        st.sidebar.write('Logistic Regression')
        st.sidebar.write('Gaussian Naive Bayes')
        st.sidebar.write('MLP')
        st.sidebar.write('Random Forest')
        st.markdown("""
		# Preliminares

A partir de una descripción estadística inicial del conjunto de datos, inferimos que algunas características de los datos son binarias u ordinales, mientras que otras características son continuas. Además, los valores mínimos y máximos para algunas características, especialmente para la presión arterial sistólica, no son realistas. Esto sugiere la presencia de valores atípicos en los datos.

Este pipeline se ejecuta utilizando el [[Feature Reduction]] y se le aplica la técnica de aumento de datos.

""")
        
        st.image(image12, width=700)
        st.image(image13, width=700)
        st.markdown("""


Como se observa en este _dataset_ luego de realizadas las modificaciones la tabla de correlaciones sugiere que no existe dependencia entre _features_. Por tanto se procedió a la ejecución de los modelos con su uso.

# Modelos y evaluación

## SVM

""")
        
        st.image(image14, width=700)
        st.markdown("""


```
__________________precision    recall  f1-score   support

         0.0       0.78      0.77      0.78       235
         1.0       0.78      0.78      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Logistic Regression
""")
        
        st.image(image15, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.80      0.81      0.81       262
         1.0       0.76      0.75      0.75       209

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## # K-Fold Cross Validation

""")
        
        st.image(image16, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.78      0.77      0.78       235
         1.0       0.78      0.78      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Gaussian Naive Bayes

""")
        
        st.image(image17, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.74      0.76      0.75       235
         1.0       0.75      0.74      0.75       236

    accuracy                           0.75       471
   macro avg       0.75      0.75      0.75       471
weighted avg       0.75      0.75      0.75       471
```

## MLP

""")
        
        st.image(image18, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.93      0.83      0.88       235
         1.0       0.85      0.94      0.89       236

    accuracy                           0.89       471
   macro avg       0.89      0.89      0.89       471
weighted avg       0.89      0.89      0.89       471
```

## KNN

""")
        
        st.image(image19, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.86      0.75      0.80       235
         1.0       0.78      0.87      0.82       236

    accuracy                           0.81       471
   macro avg       0.82      0.81      0.81       471
weighted avg       0.82      0.81      0.81       471
```

## Random Forest

""")
        
        st.image(image20, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.97      0.93      0.95       235
         1.0       0.93      0.97      0.95       236

    accuracy                           0.95       471
   macro avg       0.95      0.95      0.95       471
weighted avg       0.95      0.95      0.95       471
```
""")
    elif page == "/Pipeline 1.2":
        st.sidebar.success("Pipeline 1.2")
        st.sidebar.write('Balance de los datos')
        st.sidebar.write('Correlación')
        st.sidebar.write('Distribución de los datos')
        st.sidebar.write('SVC')
        st.sidebar.write('Logistic Regression')
        st.sidebar.write('Random Forest')
        st.sidebar.write('Gaussian Naive Bayes')
        st.sidebar.write('MLP')
        st.sidebar.write('KNN')
        st.markdown("""
                        # Preliminares

## Balance de los datos
""")
        
        st.image(image21, width=700)
        st.markdown("""

## Correlación
""")
        
        st.image(image22, width=700)
        st.markdown("""

## Distribución de los datos
""")
        
        st.image(image23, width=700)
        st.markdown("""

# Modelos y evaluación:

## SVC
""")
        
        st.image(image24, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.83      0.80      0.81       235
         1.0       0.80      0.83      0.82       236

    accuracy                           0.82       471
   macro avg       0.82      0.82      0.82       471
weighted avg       0.82      0.82      0.82       471
```

## Logistic Regression
""")
        
        st.image(image25, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.79      0.84      0.82       262
         1.0       0.78      0.73      0.75       209

    accuracy                           0.79       471
   macro avg       0.79      0.78      0.79       471
weighted avg       0.79      0.79      0.79       471
```

## Random Forest
""")
        
        st.image(image26, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.98      0.92      0.95       235
         1.0       0.92      0.98      0.95       236

    accuracy                           0.95       471
   macro avg       0.95      0.95      0.95       471
weighted avg       0.95      0.95      0.95       471
```

# K-Fold Cross Validation

## SVM
""")
        
        st.image(image27, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.83      0.80      0.81       235
         1.0       0.80      0.83      0.82       236

    accuracy                           0.82       471
   macro avg       0.82      0.82      0.82       471
weighted avg       0.82      0.82      0.82       471
```

## Gaussian Naive Bayes
""")
        
        st.image(image28, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.72      0.80      0.76       235
         1.0       0.78      0.69      0.73       236

    accuracy                           0.74       471
   macro avg       0.75      0.74      0.74       471
weighted avg       0.75      0.74      0.74       471
```

## MLP
""")
        
        st.image(image29, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.93      0.88      0.91       235
         1.0       0.89      0.94      0.91       236

    accuracy                           0.91       471
   macro avg       0.91      0.91      0.91       471
weighted avg       0.91      0.91      0.91       471
```

## KNN
""")
        
        st.image(image30, width=700)
        st.markdown("""

```
Cross-validation score means:  0.7834219858156029
Accuracy:  0.9278131634819533
__________________precision    recall  f1-score   support

         0.0       1.00      0.86      0.92       235
         1.0       0.87      1.00      0.93       236

    accuracy                           0.93       471
   macro avg       0.94      0.93      0.93       471
weighted avg       0.94      0.93      0.93       471

```
			""")
    elif page == "/Pipeline 1.3":
        st.sidebar.success("Pipeline 1.3")
        st.sidebar.success("Pipeline 1.2")
        st.sidebar.write('Balance')
        st.sidebar.write('Correlación')
        st.sidebar.write('Distribución de los datos')
        st.sidebar.write('Esparcimiento')
        st.sidebar.write('SVC')
        st.sidebar.write('Logistic Regression')
        st.sidebar.write('Random Forest')
        st.sidebar.write('Gaussian Naive Bayes')
        st.sidebar.write('MLP')
        st.sidebar.write('KNN')
        st.markdown("""
                    # Preliminares

## Balance
""")
        
        st.image(image31, width=700)
        st.markdown("""

## Correlación
""")
        
        st.image(image32, width=700)
        st.markdown("""

## Distribución

""")
        
        st.image(image33, width=700)
        st.markdown("""

## Esparcimiento
""")
        
        st.image(image34, width=700)
        st.markdown("""

# Modelos y evaluación

## SVC
""")
        
        st.image(image35, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.77      0.79      0.78       235
         1.0       0.78      0.77      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Logistic Regression
""")
        
        st.image(image36, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.81      0.84      0.82       262
         1.0       0.78      0.75      0.76       209

    accuracy                           0.80       471
   macro avg       0.79      0.79      0.79       471
weighted avg       0.80      0.80      0.80       471
```

## Random Forest
""")
        
        st.image(image37, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.95      0.94      0.94       235
         1.0       0.94      0.95      0.95       236

    accuracy                           0.94       471
   macro avg       0.94      0.94      0.94       471
weighted avg       0.94      0.94      0.94       471
```

# K-Fold Cross Validation

## SVM

""")
        
        st.image(image38, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.77      0.79      0.78       235
         1.0       0.78      0.77      0.78       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Gaussian Naive Bayes

""")
        
        st.image(image39, width=700)
        st.markdown("""

```
```
__________________precision    recall  f1-score   support

         0.0       0.68      0.80      0.73       235
         1.0       0.76      0.62      0.68       236

    accuracy                           0.71       471
   macro avg       0.72      0.71      0.71       471
weighted avg       0.72      0.71      0.71       471
```

## MLP

""")
        
        st.image(image40, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.94      0.86      0.90       235
         1.0       0.87      0.94      0.91       236

    accuracy                           0.90       471
   macro avg       0.90      0.90      0.90       471
weighted avg       0.90      0.90      0.90       471
```

## KNN

""")
        
        st.image(image41, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.98      0.84      0.90       235
         1.0       0.86      0.98      0.92       236

    accuracy                           0.91       471
   macro avg       0.92      0.91      0.91       471
weighted avg       0.92      0.91      0.91       471
```

## Random Forest

""")
        
        st.image(image42, width=700)
        st.markdown("""

```
__________________precision    recall  f1-score   support

         0.0       0.96      0.92      0.94       235
         1.0       0.93      0.96      0.94       236

    accuracy                           0.94       471
   macro avg       0.94      0.94      0.94       471
weighted avg       0.94      0.94      0.94       471
```

## Logistic Regression

""")
        
        st.image(image43, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.74      0.79      0.76       235
         1.0       0.78      0.72      0.75       236

    accuracy                           0.76       471
   macro avg       0.76      0.76      0.76       471
weighted avg       0.76      0.76      0.76       471
```

                    """)
    elif page == "/Pipeline 1.4":
        st.sidebar.success("Pipeline 1.4")
        st.markdown("""
                    # Preliminares

## Balance

""")
        image='picture/Pasted image 20230622100233.png'
        st.image(image, width=700)
        st.markdown("""
## Correlación

""")
        image='picture/Pasted image 20230622100956.png'
        st.image(image, width=700)
        st.markdown("""
## Esparcimiento

""")
        image='picture/Pasted image 20230622101027.png'
        st.image(image, width=700)
        st.markdown("""
## Distribución

""")
        image='picture/Pasted image 20230622101117.png'
        st.image(image, width=700)
        st.markdown("""
# Modelos y evaluación

## SVM


""")
        image='picture/Pasted image 20230622101236.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       1.00      0.36      0.53        22

    accuracy                           0.94       252
   macro avg       0.97      0.68      0.75       252
weighted avg       0.95      0.94      0.93       252
```

## Random Forest

""")
        image='picture/Pasted image 20230622101343.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.93      0.98      0.96       230
         1.0       0.60      0.27      0.37        22

    accuracy                           0.92       252
   macro avg       0.77      0.63      0.67       252
weighted avg       0.90      0.92      0.91       252
```

## Logistic Regression


""")
        image='picture/Pasted image 20230622101446.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.95      0.98      0.97       232
         1.0       0.64      0.45      0.53        20

    accuracy                           0.94       252
   macro avg       0.80      0.71      0.75       252
weighted avg       0.93      0.94      0.93       252
```

# K-Fold Cross Validation

## SVM

""")
        image='picture/Pasted image 20230622101602.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       1.00      0.36      0.53        22

    accuracy                           0.94       252
   macro avg       0.97      0.68      0.75       252
weighted avg       0.95      0.94      0.93       252
```

## Gaussian Naive Bayes


""")
        image='picture/Pasted image 20230622101656.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       1.00      0.33      0.50       230
         1.0       0.12      1.00      0.22        22

    accuracy                           0.39       252
   macro avg       0.56      0.67      0.36       252
weighted avg       0.92      0.39      0.47       252
```

## MLP

""")
        image='picture/Pasted image 20230622101743.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.95      0.94      0.95       230
         1.0       0.44      0.50      0.47        22

    accuracy                           0.90       252
   macro avg       0.70      0.72      0.71       252
weighted avg       0.91      0.90      0.90       252
```

## KNN


""")
        image='picture/Pasted image 20230622101818.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.95      0.97      0.96       230
         1.0       0.62      0.45      0.53        22

    accuracy                           0.93       252
   macro avg       0.79      0.71      0.74       252
weighted avg       0.92      0.93      0.92       252
```

## Random Forest


""")
        image='picture/Pasted image 20230622101947.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.95      0.99      0.97       230
         1.0       0.83      0.45      0.59        22

    accuracy                           0.94       252
   macro avg       0.89      0.72      0.78       252
weighted avg       0.94      0.94      0.94       252
```

## Logistic Regression

""")
        image='picture/Pasted image 20230622102022.png'
        st.image(image, width=700)
        st.markdown("""
```
__________________precision    recall  f1-score   support

         0.0       0.95      0.97      0.96       230
         1.0       0.62      0.45      0.53        22

    accuracy                           0.93       252
   macro avg       0.79      0.71      0.74       252
weighted avg       0.92      0.93      0.92       252
```
""")
display_page(PAGES[selection])
		