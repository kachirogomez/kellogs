import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

#producto1 = pd.read_csv('tiendaspaketitofroot.csv',delimiter=' ')

#print(producto1.head())
#print(producto1.describe(include="all"))

#histo = producto1.rSales.hist(bins=100)

#histo.set_title("Paketito Froot Loops")
# Set x-axis label
#histo.set_xlabel("Ventas", labelpad=20, size=12)

# Set y-axis label
#histo.set_ylabel("Frecuencia", labelpad=20, size=12)

#plt.show()

#nombres = []
#for col in producto1.columns:
#	nombres.append(col)

#print(nombres)

#script_dir = os.getcwd()
#file = 'AGEBCDMX.csv'

#cdmx = pd.read_csv('AGEBCDMX.csv',encoding='latin1',delimiter=' ')
#os.path.normcase(os.path.join(script_dir, file))
#print(cdmx.head())
#print(cdmx.describe(include="all"))

import shapefile
shape = shapefile.Reader('09a.shp')
#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__  
print(first) # (GeoJSON format)

#coord = feature.shape.points[:]

#print(coord[0])

plt.figure()
#for i in range(len(coord)):
#	x1 = [j[0] for j in coord]
#	y1 = [j[1] for j in coord]
#	plt.plot(x1,y1)

coord = []

for shape in shape.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    xy = [x,y]
    coord.append(xy)
    plt.plot(x,y)

m = np.matrix(coord)
df = pd.DataFrame(data=m)
df.to_csv('coordenadasINEGI.csv', sep=' ', header=False, index=False)

#print(coord)
#print(len(coord))

#shape2 = shapefile.Reader('09ar.shp')

#for shape in shape2.shapeRecords():
#    x = [i[0] for i in shape.shape.points[:]]
#    y = [i[1] for i in shape.shape.points[:]]
#    plt.plot(x,y)

#shape3 = shapefile.Reader('09cd.shp',encoding='latin1')

#for shape in shape3.shapeRecords():
#    x = [i[0] for i in shape.shape.points[:]]
#    y = [i[1] for i in shape.shape.points[:]]
#    plt.plot(x,y)

#shape4 = shapefile.Reader('09e.shp',encoding='latin1')

#for shape in shape4.shapeRecords():
#    x = [i[0] for i in shape.shape.points[:]]
#    y = [i[1] for i in shape.shape.points[:]]
#    plt.plot(x,y)

plt.show()

#CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
#                       'embark_town', 'alone']
#NUMERIC_COLUMNS = ['age', 'fare']

