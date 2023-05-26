import pandas as pd
import random as rand

def complete_fixed__creatinina__01(original_table, new_table, directory='default_values/'):

    mean_creatinina = pd.read_csv(f'{directory}creatinina.csv')['creatinina'][0]
    nan_values = original_table['creatinina'].isna()
    for i in range(original_table.shape[0]):
        if nan_values[i]:
            new_table['creatinina'].iloc[i] = mean_creatinina        
    new_table['creatinina'].describe()

def complete_fixed__hb__01(original_table, new_table, directory='default_values/'):

    media_hb = pd.read_csv(f'{directory}hb.csv')
    nan_values = original_table['hb'].isna()
    for i in range(original_table.shape[0]):
        if nan_values[i]:        
            a = original_table['sexo'].iloc[i]        
            b = media_hb['hb'].iloc[int(a)]        
            new_table['hb'].iloc[i] = b

def complete_unfixed__hb__01(original_table, new_table, directory='default_values/'):

    media_hb = pd.read_csv(f'{directory}hb.csv')
    nan_values = original_table['hb'].isna()
    for i in range(original_table.shape[0]):
        if nan_values[i]:        
            a = original_table['sexo'].iloc[i]        
            b = media_hb['hb'].iloc[int(a)] 
            # Distribuci'on normal de la hemoglobina, con la media conocida, y desviaci'on 7
            rand_hb = rand.gauss(b,7)
            new_table['hb'].iloc[i] = rand_hb

def complete_fixed__ckmb__01(original_table, new_table, directory='default_values/'):

    mean_ckmb = pd.read_csv(f'{directory}ckmb.csv')
    nan_values = original_table['ckmb'].isna()
    for i in range(original_table.shape[0]):
        if nan_values[i]:  
            if original_table['infarto_miocardio_agudo'].iloc[i] == 0:
                if original_table['sexo'].iloc[0] == 0: # Mujer
                    new_table['ckmb'].iloc[i] = mean_ckmb['WOMAN_mean_STEMI']
                else:
                    new_table['ckmb'].iloc[i] = mean_ckmb['MEN_mean_STEMI']
            else:
                if original_table['sexo'].iloc[0] == 0: # Mujer
                    new_table['ckmb'].iloc[i] = mean_ckmb['WOMAN_mean_NSTEMI']
                else:
                    new_table['ckmb'].iloc[i] = mean_ckmb['MEN_mean_NSTEMI']

def complete_fixed__ckmb__02(original_table, new_table, directory='default_values/'):
    '''
    Rellenado del `ckmb` por `infarto_miocardio_agudo`, con las
    medias de los valores limpios
    '''
    mean_ckmb = pd.read_csv(f'{directory}ckmb.csv')
    nan_values = original_table['ckmb'].isna()
    for i in range(original_table.shape[0]):
        if nan_values[i]:  
            if original_table['infarto_miocardio_agudo'].iloc[i] == 0:                
                new_table['ckmb'].iloc[i] = 136.15893108298172
            else:
                new_table['ckmb'].iloc[i] = 112.1948051948052