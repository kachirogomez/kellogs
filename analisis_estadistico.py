import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

producto1 = pd.read_csv('tiendaspaketitofroot.csv',delimiter=' ')

print(producto1.head())
print(producto1.describe(include="all"))

producto1.rSales.hist(bins=100)
plt.show()

nombres = []
for col in producto1.columns:
	nombres.append(col)

print(nombres)


