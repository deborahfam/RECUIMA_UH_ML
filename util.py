import pandas as pd

def z_score(x, mean=None, std=None):
    '''
    Calcula el puntaje `z` para saber la cantidad de desviaciones
    tienen los datos de la media.
    ---
    Si `x` es un n'umero, se debe proporcionar la media `mean` y la
    desviaci'on est'andar `std`.

    Si `x` es una `pd.Series` se calcula el `z-score` de cada dato
    con respecto a la media y desvaci'on de estos

    Si `x` es un `pd.Pandas` se calcula el `z-score` de cada dato
    analizando por columnas las medias y desviaciones estandar
    '''
    if type(x) is pd.DataFrame:        
        return x.apply(z_score, axis=1)
    elif type(x) is pd.Series:
        mean = x.mean()
        std = x.std()
        return (x-mean)/std
    return (x-mean)/std

def z_score_abs(x, mean=None, std=None):
    '''
    Calcula el m'odulo del puntaje `z` para saber la cantidad de desviaciones
    modulares que tienen los datos de la media.
    ---
    Consulte el m'etodo `z_score`, para m'as detalles de los par'ametros
    '''
    return abs(z_score(x))

def non_outlier_data(table, feauture, umbral=3, reset_index=True): 
    '''
    Elimina las filas de una tabla, que tengan valores por encima de cierto
    umbral, de `puntaje-z` de una caracter'istica dada
    ---
    `table`: Tabla de valores tipo `pd.DataFrame`

    `feauture`: Nombre de la columna a la que se le eliminar'an los valores at'ipicos

    `umbral`: Escalar mayor que `0` que indica la tolerancia m'axima permitida

    `reset_index`: Si est'a en `True` reinicia los 'indices de la tabala. En caso
    contrario los deja como estaban.

    '''   
    clean = table.where(z_score_abs(table[feauture])<=umbral).dropna(axis=0, how='all')
    if reset_index:
        clean.reset_index(drop=True, inplace=True)
    return clean