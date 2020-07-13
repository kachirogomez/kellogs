import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

import folium
from folium.plugins import FastMarkerCluster

import pyproj
from pyproj import CRS

#Parte de transformar coordenadas

crs = CRS.from_proj4('+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m no_defs')
#print(crs)
crs2 = CRS.from_epsg(3857)
#print(crs2.geodetic_crs)
proj = pyproj.transformer.Transformer.from_crs(crs, crs2.geodetic_crs)
#t = proj.transform(2792293.082599997,836437.284)
#print(t[0])
#print(proj.transform(2792293.082599997,836437.284))

import shapefile
shape = shapefile.Reader('09a.shp')
#print(shape)
#print(shape.bbox)
#first feature of the shapefile
#feature = shape.shapeRecords()[0]
#first = feature.shape.__geo_interface__  
#print(first) # (GeoJSON format)

#coord = []
coord2 = []
coort = []

for shape in shape.shapeRecords():
	for i in shape.shape.points[:]:
		t = proj.transform(i[0],i[1])
		x = t[0]
		y = t[1]
		xy = [x,y]
#		n = (x,y)
#		coord.append(xy)
		coort.append(xy)
	coord2.extend([coort])
	coort = []
#    plt.plot(x,y)
#    coord.append(shape.shape.points[:])

m = np.array(coord2)
#print(m)
#print(m.size)
df = pd.DataFrame(data=m)
df.to_csv('sintuplasINEGI.csv', sep=' ', header=False, index=False)

#print(coord[0])
#print(coord2[0])
#print(coord2[1])
#print(len(coord2))

#Crear el mapa como un objeto
#m = folium.Map(location=[19.595772, -98.997218])

#from openpyxl import load_workbook

#wb = load_workbook('coordenadas.xlsx')
#sheet = wb.worksheets[0]

#coordenadas = []

#for row in sheet.iter_rows(min_row=2,values_only=True):
#	xy = [ row[0] , row[1]]
#	if xy not in coordenadas:
#		coordenadas.append(xy)

#folium.plugins.FastMarkerCluster(coordenadas,name='Tiendas de conveniencia').add_to(m)

#folium.plugins.FastMarkerCluster(coord,name='AGEB').add_to(m)

#folium.map.LayerControl().add_to(m)

#m.save('completo.html')
