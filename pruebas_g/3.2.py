from __future__ import absolute_import, division, print_function, unicode_literals

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

#rank1_tensor = tf.Variable(["test","ok"], tf.string)
#rank2_tensor = tf.Variable([["test","ok"],["test","yes"]], tf.string)
#print(tf.rank(rank1_tensor))
#print(rank2_tensor.shape)

t = tf.zeros([5,5,5,5])
#print(t)

t = tf.reshape(t,[125,-1])
#print(t)

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') #training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
#print(dftrain.head())

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

#print(dftrain.head())
#print(y_train)

#plt.show(dftrain.age.hist(bins=20))
#plt.show(dftrain.sex.value_counts().plot(kind='barh'))
#plt.show(dftrain['class'].value_counts().plot(kind='barh'))
#plt.show(pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive'))

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)