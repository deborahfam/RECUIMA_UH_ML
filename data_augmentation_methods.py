import random as rand
import pandas as pd
import numpy as np
from math import inf
import json

def noise_uniform(mean, std, min_value=-inf, max_value=inf):
    return rand.uniform(max(mean-std, min_value), min(mean+std, max_value))

def switch_noise_methods(name):
    if name == 'uniform':
        return noise_uniform
    else:
        raise Exception('Metodo de ruido no encontrado')

def create_mod_record(origin_record, features):
    new_record = origin_record.copy()    

    for feature, methods in features.items():
        method = switch_noise_methods(methods['method'])
        args = methods['args']
        new_record[feature] = method(origin_record[feature], *args)

    return new_record

def create_many_mod_record(n, table : pd.DataFrame, features):

    sample = table.sample(n=n, replace= True)    
    return sample.apply(lambda record: create_mod_record(record, features), axis=1)

def create_many_mod_record_from_json(n, table : pd.DataFrame, features_path):
    with open(features_path, 'rb') as fp:
        features = json.load(fp)
        return create_many_mod_record(n,table, features)
