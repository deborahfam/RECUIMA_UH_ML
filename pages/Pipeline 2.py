import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )
image12='picture/image12.png'
image13='picture/image13.png'
image14='picture/image14.png'
image15='picture/image15.png'
image16='picture/image16.png'
image17='picture/image17.png'
image18='picture/image18.png'
image19='picture/image19.png'
image20='picture/image20.png'
image21='picture/image21.png'
image22='picture/image22.png'
image23='picture/image23.png'
image24='picture/image24.png'
image25='pictures2/output1.png'
image26='picture/Pasted image 20230622064137.png'
image27='picture/Pasted image 20230622102849.png'
image28='picture/Pasted image 20230622103117.png'
image29='picture/Pasted image 20230622063922.png'
image30='picture/Pasted image 20230622064040.png'
image31='picture/Pasted image 20230622064429.png'
st.set_page_config(page_title="RECUIMA", layout="wide")
PAGES = {
    "Pipeline 2": "/Pipeline 2",
    "Pipeline 2.1": "/Pipeline 2.1",
    "Pipeline 2.2":"/Pipeline 2.2",
    "Pipeline 2.3":"/Pipeline 2.3",
    "Pipeline 2.4":"/Pipeline 2.4",
}
selection = st.sidebar.radio("", list(PAGES.keys()))
def display_page(page):
   if page == "/Pipeline 2":
        st.sidebar.success("Pipeline 2")
        st.sidebar.write('weight = "balanced"')
        st.sidebar.write('Subsampling')
        st.sidebar.write('Oversampling')
        st.sidebar.write('Resampling con SMOTE + Tomek')
        st.sidebar.write('Ensamble de modelos')
        
        st.markdown("""
               # Primera forma de balance de pesos
        
        Utilizando un parámetro adicional donde indicamos weight = "balanced" en el modelo de Regresión Logística y otros que lo permiten, con esto el algoritmo se encargará de equilibrar la clase minoritaria durante el entrenamiento.
        
        """)
        st.markdown("""## Logistic Regression
        """)
        st.image(image12, width=700)
        st.markdown("""
                    
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.97      0.72      0.82       239
                   1       0.28      0.81      0.41        32
        
            accuracy                           0.73       271
           macro avg       0.62      0.76      0.62       271
        weighted avg       0.88      0.73      0.77       271
        ```
        """)
        st.markdown("""## SVM""")
        
        st.image(image13, width=700)
        st.markdown("""
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.96      0.74      0.83       239
                   1       0.28      0.75      0.40        32
        
            accuracy                           0.74       271
           macro avg       0.62      0.74      0.62       271
        weighted avg       0.88      0.74      0.78       271
        ```
        """)
        st.markdown("""## Random Forest""")
        
        st.image(image14, width=700)
        st.markdown("""
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.90      0.98      0.94       239
                   1       0.55      0.19      0.28        32
        
            accuracy                           0.89       271
           macro avg       0.72      0.58      0.61       271
        weighted avg       0.86      0.89      0.86       271
        ```
        
        # Subsampling en la clase mayoritaria
        
        Se realiza esto para disminuir la cantidad de elemento en la clase mayoritaria e intentar balancear de otra forma el _dataset_.""")
        st.markdown("""## Logistic Regression""")
        
        st.image(image15, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.93      0.34      0.50       239
                   1       0.14      0.81      0.24        32
        
            accuracy                           0.40       271
           macro avg       0.54      0.58      0.37       271
        weighted avg       0.84      0.40      0.47       271
        ```
        """)
        st.markdown("""## SVM""")
        
        st.image(image16, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.83      0.14      0.24       239
                   1       0.11      0.78      0.19        32
        
            accuracy                           0.22       271
           macro avg       0.47      0.46      0.22       271
        weighted avg       0.74      0.22      0.24       271
        ```
        """)
        st.markdown("""## Random Forest""")
        
        st.image(image17, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.98      0.36      0.52       239
                   1       0.16      0.94      0.28        32
        
            accuracy                           0.42       271
           macro avg       0.57      0.65      0.40       271
        weighted avg       0.88      0.42      0.49       271
        ```
        
        # Oversampling en la clase minoritaria
        
        Con esto se aumentan los datos en la clase minoritaria en otro intento por balancear el _dataset_.
        """)
        st.markdown("""## Logistic Regression""")
        
        st.image(image18, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.96      0.86      0.91       239
                   1       0.40      0.72      0.52        32
        
            accuracy                           0.84       271
           macro avg       0.68      0.79      0.71       271
        weighted avg       0.89      0.84      0.86       271
        ```
        
        
        """)
        st.markdown("""## SVM""")
        
        st.image(image19, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.96      0.73      0.83       239
                   1       0.27      0.75      0.40        32
        
            accuracy                           0.73       271
           macro avg       0.61      0.74      0.61       271
        weighted avg       0.88      0.73      0.78       271
        ```
        """)
        st.markdown("""## Random Forest""")
        
        st.image(image20, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.92      0.97      0.95       239
                   1       0.67      0.38      0.48        32
        
            accuracy                           0.90       271
           macro avg       0.79      0.67      0.71       271
        weighted avg       0.89      0.90      0.89       271
        ```
        
        # Resampling con SMOTE + Tomek
        
        Ahora probaremos una técnica ampliamente utilizada que consiste en aplicar simultáneamente un algoritmo de submuestreo y un algoritmo de sobremuestreo al conjunto de datos al mismo tiempo. En este caso, usaremos SMOTE para el sobremuestreo: encuentre puntos vecinos cercanos y agregue puntos "en línea recta" entre ellos. Y usaremos Tomek para el submuestreo que elimina los de diferentes clases que son vecinos más cercanos y nos permite ver mejor el límite de decisión (la zona límite de nuestras clases).
        
        """)
        st.markdown("""## Logistic Regression""")
        
        st.image(image21, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.95      0.85      0.90       239
                   1       0.38      0.69      0.49        32
        
            accuracy                           0.83       271
           macro avg       0.67      0.77      0.69       271
        weighted avg       0.89      0.83      0.85       271
        ```
        
        """)
        st.markdown("""## SVM""")
        
        st.image(image22, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.95      0.74      0.83       239
                   1       0.27      0.72      0.39        32
        
            accuracy                           0.74       271
           macro avg       0.61      0.73      0.61       271
        weighted avg       0.87      0.74      0.78       271
        ```
        
        """)
        st.markdown("""## Random Forest""")
        
        st.image(image23, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.93      0.96      0.94       239
                   1       0.58      0.44      0.50        32
        
            accuracy                           0.90       271
           macro avg       0.76      0.70      0.72       271
        weighted avg       0.89      0.90      0.89       271
        ```
        
        # Ensamble de modelos
        
        Otra forma de intentar balancear las clases del _dataset_.
        
        ## Balanced Bagging
        
        """)
        st.image(image24, width=700)
        st.markdown("""
        
        ```
        _________________precision    recall  f1-score   support
        
                   0       0.96      0.80      0.87       239
                   1       0.33      0.75      0.46        32
        
            accuracy                           0.79       271
           macro avg       0.65      0.77      0.67       271
        weighted avg       0.89      0.79      0.82       271
        ```
        """)
   elif page == "/Pipeline 2.1":
      st.sidebar.success("Pipeline 2.1")
      st.markdown("""# Preliminares

En este pipeline se trabaja con [[Improved Dataset]], además también se aplica el balance de pesos y la técnica para aumento de datos.

# Modelos y evaluación

## Balanced Weights

### Logistic Regression

""")
      st.image(image25, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

           0       0.97      0.70      0.81       239
           1       0.27      0.81      0.40        32

    accuracy                           0.71       271
   macro avg       0.62      0.76      0.61       271
weighted avg       0.88      0.71      0.76       271
```

### SVM

""")
      image='pictures2/output2.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

           0       0.94      0.32      0.48       239
           1       0.14      0.84      0.24        32

    accuracy                           0.38       271
   macro avg       0.54      0.58      0.36       271
weighted avg       0.85      0.38      0.45       271
```

### Random Forest

""")
      st.image(image27, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       0.89      0.36      0.52        22

    accuracy                           0.94       252
   macro avg       0.92      0.68      0.74       252
weighted avg       0.94      0.94      0.93       252
```

### Near Miss

""")
      st.image(image28, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Subsampling

### Logistic Regression

""")
      st.image(image29, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.72      0.75      0.74       235
         1.0       0.74      0.71      0.72       236

    accuracy                           0.73       471
   macro avg       0.73      0.73      0.73       471
weighted avg       0.73      0.73      0.73       471
```

### SVM

""")
      st.image(image30, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.79      0.77      0.78       235
         1.0       0.78      0.79      0.79       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

```""")
   elif page == "/Pipeline 2.2":
      st.sidebar.success("Pipeline 2.2")
      st.markdown("""
                  # Modelos y evaluación

## Balanced Weights

### Logistic Regression

""")
      image='pictures2/output3.png'
      st.image(image, width=700)
      st.markdown("""

```
_________________precision    recall  f1-score   support

           0       0.97      0.70      0.81       239
           1       0.27      0.81      0.40        32

    accuracy                           0.71       271
   macro avg       0.62      0.76      0.61       271
weighted avg       0.88      0.71      0.76       271
```

### SVM

""")
      image='picture/Pasted image 20230622110343.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

## Random Forest


""")
      image='picture/Pasted image 20230622110821.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.94      1.00      0.97       230
         1.0       0.89      0.36      0.52        22

    accuracy                           0.94       252
   macro avg       0.92      0.68      0.74       252
weighted avg       0.94      0.94      0.93       252
```

## Subsampling

### Logistic Regression

""")
      image='picture/Pasted image 20230622110047.png'
      st.image(image, width=700)
      st.markdown("""
                  
```
_________________precision    recall  f1-score   support

         0.0       0.72      0.75      0.74       235
         1.0       0.74      0.71      0.72       236

    accuracy                           0.73       471
   macro avg       0.73      0.73      0.73       471
weighted avg       0.73      0.73      0.73       471
```

### SVM


""")
      image='picture/Pasted image 20230622110723.png'
      st.image(image, width=700)
      st.markdown("""
                  
```
_________________precision    recall  f1-score   support

         0.0       0.79      0.77      0.78       235
         1.0       0.78      0.79      0.79       236

    accuracy                           0.78       471
   macro avg       0.78      0.78      0.78       471
weighted avg       0.78      0.78      0.78       471
```

## Random Forest

""")
      image='picture/Pasted image 20230622110932.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Conjunto de modelos con Balanced Bagging


""")
      image='picture/Pasted image 20230622110200.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```

""")
   elif page == "/Pipeline 2.3":
      st.sidebar.success("Pipeline 2.3")
      st.markdown("""# Modelos y evaluación

## Balanced Weights

### Logistic Regression

""")
      image='picture/Pasted image 20230622111437.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.99      0.85      0.91       230
         1.0       0.36      0.91      0.52        22

    accuracy                           0.85       252
   macro avg       0.68      0.88      0.72       252
weighted avg       0.94      0.85      0.88       252
```

### SVM


""")
      image='picture/Pasted image 20230622111838.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

### Random Forest

""")
      image='picture/Pasted image 20230622112009.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.93      1.00      0.97       230
         1.0       1.00      0.27      0.43        22

    accuracy                           0.94       252
   macro avg       0.97      0.64      0.70       252
weighted avg       0.94      0.94      0.92       252
```

## Subsampling

### Logistic Regression
""")
      image='picture/Pasted image 20230622111624.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.97      0.55      0.70       230
         1.0       0.15      0.82      0.25        22

    accuracy                           0.58       252
   macro avg       0.56      0.69      0.48       252
weighted avg       0.90      0.58      0.66       252
```

### SVM

""")
      image='picture/Pasted image 20230622111918.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.56      0.71       230
         1.0       0.16      0.86      0.27        22

    accuracy                           0.58       252
   macro avg       0.57      0.71      0.49       252
weighted avg       0.91      0.58      0.67       252
```

### Random Forest

""")
      image='picture/Pasted image 20230622112158.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.99      0.78      0.87       230
         1.0       0.29      0.91      0.43        22

    accuracy                           0.79       252
   macro avg       0.64      0.85      0.65       252
weighted avg       0.93      0.79      0.84       252
```

## Conjunto de modelos con Balanced Bagging

""")
      image='picture/Pasted image 20230622111709.png'
      st.image(image, width=700)
      st.markdown("""
```
_________________precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```

## SNN

""")
      image='picture/Pasted image 20230622113225.png'
      st.image(image, width=700)
      st.markdown("""

""")
      image='picture/Pasted image 20230622113231.png'
      st.image(image, width=700)
      st.markdown("""
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
""")
   elif page == "/Pipeline 2.4":
      st.sidebar.success("Pipeline 2.4")
      st.markdown("""
                  # Modelos y evaluación

## Balanced Weights

### Logistic Regression


""")
      image='picture/Pasted image 20230622114221.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.99      0.85      0.91       230
         1.0       0.36      0.91      0.52        22

    accuracy                           0.85       252
   macro avg       0.68      0.88      0.72       252
weighted avg       0.94      0.85      0.88       252
```

### SVM

""")
      image='picture/Pasted image 20230622114443.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.98      0.90      0.94       230
         1.0       0.45      0.82      0.58        22

    accuracy                           0.90       252
   macro avg       0.72      0.86      0.76       252
weighted avg       0.93      0.90      0.91       252
```

### Random Forest

""")
      image='picture/Pasted image 20230622114616.png'
      st.image(image, width=700)
      st.markdown("""
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

""")
      image='picture/Pasted image 20230622114302.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.97      0.55      0.70       230
         1.0       0.15      0.82      0.25        22

    accuracy                           0.58       252
   macro avg       0.56      0.69      0.48       252
weighted avg       0.90      0.58      0.66       252
```

### SVM

""")
      image='picture/Pasted image 20230622114539.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.98      0.56      0.71       230
         1.0       0.16      0.86      0.27        22

    accuracy                           0.58       252
   macro avg       0.57      0.71      0.49       252
weighted avg       0.91      0.58      0.67       252
```

### Random Forest

""")
      image='picture/Pasted image 20230622114704.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.98      0.86      0.92       230
         1.0       0.37      0.86      0.51        22

    accuracy                           0.86       252
   macro avg       0.68      0.86      0.71       252
weighted avg       0.93      0.86      0.88       252
```

## Conjunto de modelos con Balanced Bagging

""")
      image='picture/Pasted image 20230622114401.png'
      st.image(image, width=700)
      st.markdown("""
```
              precision    recall  f1-score   support

         0.0       0.98      0.88      0.93       230
         1.0       0.39      0.77      0.52        22

    accuracy                           0.87       252
   macro avg       0.68      0.83      0.72       252
weighted avg       0.92      0.87      0.89       252
```
""")
display_page(PAGES[selection])
        