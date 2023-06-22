import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )
image1="picture/Pasted image 20230621231602.png"
image2="picture/Pasted image 20230621231645.png"
image3="picture/Pasted image 20230621231854.png"
image4="picture/Pasted image 20230621231919.png"
image5="picture/Pasted image 20230621232005.png"
image6="picture/Pasted image 20230622013222.png"
image7="picture/Pasted image 20230622013236.png"
image8='picture/Pasted image 20230622063032.png'
image9='picture/Pasted image 20230622063040.png'
image10='picture/Pasted image 20230622063103.png'
image11='picture/Pasted image 20230622063109.png'
st.set_page_config(page_title="RECUIMA", layout="wide")

PAGES = {
    "Pipeline 3": "/Pipeline 3",
    "Pipeline 3.1": "/Pipeline 3.1",
    "Pipeline 3.2":"/Pipeline 3.2",
    "Pipeline 3.3":"/Pipeline 3.3",
    "Pipeline 3.4":"/Pipeline 3.4",
}
selection = st.sidebar.radio("", list(PAGES.keys()))
def display_page(page):
   if page == "/Pipeline 3":
        st.sidebar.success("Pipeline 3")
        st.markdown("""# Técnicas para dividir el dataset
        
        """)
        st.markdown("""## K-Fold""")
        st.image(image1, width=700)
        st.markdown("""
        
        ## Stratified K-Fold
        """)
        st.image(image2, width=700)
        st.markdown("""
        
        ## Stratified Group K-Fold
        """)
        st.image(image3, width=700)
        st.markdown("""
        
        ## Group K-Fold
        """)
        st.image(image4, width=700)
        st.markdown("""
        
        ## Time Series Split
        """)
        st.image(image5, width=700)
        st.markdown("""
        
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
        
        ## CNN
        
        ```
        (1353, 25) 
        Epoch 1/13 73/73 [==============================] - 1s 3ms/step - loss: 0.5452 - accuracy: 0.8254 - val_loss: 0.3469 - val_accuracy: 0.9493 
        
        Epoch 2/13 73/73 [==============================] - 0s 1ms/step - loss: 0.3207 - accuracy: 0.8948 - val_loss: 0.2114 - val_accuracy: 0.9447 
        
        Epoch 3/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2677 - accuracy: 0.8948 - val_loss: 0.1886 - val_accuracy: 0.9447 
        
        Epoch 4/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2488 - accuracy: 0.8948 - val_loss: 0.1858 - val_accuracy: 0.9447 
        
        Epoch 5/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2362 - accuracy: 0.8960 - val_loss: 0.1828 - val_accuracy: 0.9447 
        
        Epoch 6/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2269 - accuracy: 0.8994 - val_loss: 0.1806 - val_accuracy: 0.9493 
        
        Epoch 7/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2192 - accuracy: 0.9110 - val_loss: 0.1767 - val_accuracy: 0.9447 
        
        Epoch 8/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2128 - accuracy: 0.9145 - val_loss: 0.1746 - val_accuracy: 0.9493 
        
        Epoch 9/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2074 - accuracy: 0.9202 - val_loss: 0.1714 - val_accuracy: 0.9493 
        
        Epoch 10/13 73/73 [==============================] - 0s 1ms/step - loss: 0.2020 - accuracy: 0.9214 - val_loss: 0.1705 - val_accuracy: 0.9493 
        
        Epoch 11/13 73/73 [==============================] - 0s 1ms/step - loss: 0.1980 - accuracy: 0.9225 - val_loss: 0.1712 - val_accuracy: 0.9493 
        
        Epoch 12/13 73/73 [==============================] - 0s 1ms/step - loss: 0.1932 - accuracy: 0.9260 - val_loss: 0.1717 - val_accuracy: 0.9447
        ```
        
        """)
        st.image(image6, width=700)
        
        st.image(image7, width=700)
        st.markdown("""
        """)
   if page == "/Pipeline 3.1":
         st.sidebar.success("Pipeline 3.1")
         st.markdown("""# Preliminares

## K-Fold
""")
         st.image(image8, width=700)
         st.markdown("""
## Stratified K-Fold
""")
         st.image(image9, width=700)
         st.markdown("""
## Stratified Group K-Fold
""")
         st.image(image10, width=700)
         st.markdown("""
## Group K-Fold
""")
         st.image(image11, width=700)
         st.markdown("""
# Modelos y evaluación

## SVC
```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9977
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9977
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9549
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9489
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9614
El resultado AUC promediado es 0.9721
```

## Gradient Boosting
```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9803
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9803
======= Fold 2 ========
El AUC en el conjunto de validación es 0.8685
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9818
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9669
El resultado AUC promediado es 0.9556
```

## Hist Gradient Boosting
```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9919
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9919
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9703
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9802
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9755
El resultado AUC promediado es 0.9820
```
""")
   if page == "/Pipeline 3.2":
         st.sidebar.success("Pipeline 3.2")
         st.markdown("""
                     # Modelos y evaluación

## SVM

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9965
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9965
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9623
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9536
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9396
El resultado AUC promediado es 0.9697
```

### Gradient Boosting

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9771
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9737
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9737
======= Fold 3 ========
El AUC en el conjunto de validación es 0.8887
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9747
El resultado AUC promediado es 0.9576
```

## Hist Gradient Boosting

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9875
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9752
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9752
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9733
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9783
El resultado AUC promediado es 0.9779
```
""")
   if page == "/Pipeline 3.3":
      st.sidebar.success("Pipeline 3.3")
      st.markdown("""
                  # Preliminares

## K-Fold

""")
      image='picture/Pasted image 20230622122106.png'
      st.image(image, width=700)
      st.markdown("""
## Stratified K-Fold
""")
      image='picture/Pasted image 20230622122116.png'
      st.image(image, width=700)
      st.markdown("""
## Stratified Group K-Fold

""")
      image='picture/Pasted image 20230622122150.png'
      st.image(image, width=700)
      st.markdown("""
## Group K-Fold
""")
      image='picture/Pasted image 20230622122157.png'
      st.image(image, width=700)
      st.markdown("""
## Time Series Split
""")
      image='picture/Pasted image 20230622122222.png'
      st.image(image, width=700)
      st.markdown("""
# Modelos y evaluación

## SVM

```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9917
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9582
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9582
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9598
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9387
El resultado AUC promediado es 0.9613
```

## Gradient Boosting
```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9917
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9459
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9459
======= Fold 3 ========
El AUC en el conjunto de validación es 0.8894
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9927
El resultado AUC promediado es 0.9531
```

## Hist Gradient Boosting
```
======= Fold 0 ========
El AUC en el conjunto de validación es 0.9854
======= Fold 1 ========
El AUC en el conjunto de validación es 0.9755
======= Fold 2 ========
El AUC en el conjunto de validación es 0.9755
======= Fold 3 ========
El AUC en el conjunto de validación es 0.9787
======= Fold 4 ========
El AUC en el conjunto de validación es 0.9820
El resultado AUC promediado es 0.9794
""")
   if page == "/Pipeline 3.4":
      st.sidebar.success("Pipeline 3.4")
      st.markdown("""
                  # Preliminares

## K-Fold
""")
      image='picture/Pasted image 20230622115044.png'
      st.image(image, width=700)
      st.markdown("""
## Stratified K-Fold
""")
      image='picture/Pasted image 20230622115135.png'
      st.image(image, width=700)
      st.markdown("""
## Stratified Group K-Fold

""")
      image='picture/Pasted image 20230622115156.png'
      st.image(image, width=700)
      st.markdown("""
## Group K-Fold
""")
      image='picture/Pasted image 20230622115216.png'
      st.image(image, width=700)
      st.markdown("""
## Times Series Split

""")
      image='picture/Pasted image 20230622115242.png'
      st.image(image, width=700)
      st.markdown("""
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

""")
      image='picture/Pasted image 20230622120723.png'
      _image='picture/Pasted image 20230622120727.png'
      st.image(image, width=700)
      st.image(_image, width=700)

      
display_page(PAGES[selection])