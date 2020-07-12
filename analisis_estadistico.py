import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

producto1 = pd.read_csv('tiendaspaketitofroot.csv',delimiter=' ')

print(producto1.head())
print(producto1.describe(include="all"))

histo = producto1.rSales.hist(bins=100)

histo.set_title("Paketito Froot Loops")
# Set x-axis label
histo.set_xlabel("Ventas", labelpad=20, size=12)

# Set y-axis label
histo.set_ylabel("Frecuencia", labelpad=20, size=12)

plt.show()

nombres = []
for col in producto1.columns:
	nombres.append(col)

print(nombres)

#script_dir = os.getcwd()
#file = 'AGEBCDMX.csv'

cdmx = pd.read_csv('AGEBCDMX.csv',encoding='latin1',delimiter=' ')
#os.path.normcase(os.path.join(script_dir, file))
print(cdmx.head())
print(cdmx.describe(include="all"))

#CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
#                       'embark_town', 'alone']
#NUMERIC_COLUMNS = ['age', 'fare']

