import streamlit as st
import pandas as pd

# st.set_page_config(
#         page_title="RECUIMA",
#     )
st.set_page_config(page_title="RECUIMA", layout="wide")

st.sidebar.success("Pipeline 4")
st.markdown("""
            ## SNN

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
image='picture/Pasted image 20230622013222.png'
st.image(image)
image='picture/Pasted image 20230622013236.png'
st.image(image)
st.markdown("""
# SNN con SMOTE + Tomek
""")

image='picture/Pasted image 20230622132419.png'
st.image(image)

image='picture/Pasted image 20230622132422.png'
st.image(image)
st.markdown("""
```

______________precision    recall  f1-score   support

           0       0.96      0.86      0.91       236
           1       0.45      0.74      0.56        35

    accuracy                           0.85       271
   macro avg       0.70      0.80      0.73       271
weighted avg       0.89      0.85      0.86       271
""")

