import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import tensorflow as tf

#Este pos es pa los mapas
import folium
from folium.plugins import FastMarkerCluster

#Este paquete es para transformar las coordenadas
import pyproj
from pyproj import CRS

#Parte de transformar coordenadas

#Este crs son las de la proyección de Lambert (LCC)
crs = CRS.from_proj4('+proj=lcc +lat_1=17.5 +lat_2=29.5 +lat_0=12 +lon_0=-102 +x_0=2500000 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m no_defs')
#print(crs)
#Este crs2 es de las coordenadas del GPS
crs2 = CRS.from_epsg(3857)
#print(crs2.geodetic_crs)
#Aquí creas un transformador que vaya de las LCC a las de GPS
proj = pyproj.transformer.Transformer.from_crs(crs, crs2.geodetic_crs)
#Igual los prints de aquí abajo namas fueron pruebas
#t = proj.transform(2792293.082599997,836437.284)
#print(t[0])
#print(proj.transform(2792293.082599997,836437.284))

#Parte de leer el .shp
import shapefile
shape = shapefile.Reader('09a.shp')
#Los prints de aquí abajo namas fueron pruebas también
#print(shape)
#print(shape.bbox)
#first feature of the shapefile
#feature = shape.shapeRecords()[0]
#first = feature.shape.__geo_interface__  
#print(first) # (GeoJSON format)

#La lista coord es para el mapa y la lista coord2 es para el csv
#Son 2 diferentes porque la lista coord trae los puntos en una sola línea
#Y la lista coord2 si los trae por polígono
#La lista coort namas es un auxiliar para poder llenar la coord2
#coord = []
coord2 = []
coort = []


#Es lo mismo que en los otros casos, namas lee el archivo con el for 
#Trae varias cosas comentadas como la variabe n =(x,y) porque estuve calando con otros métodos
for shape in shape.shapeRecords():
	for i in shape.shape.points[:]:
        #El t es donde se transforman las coordenadas de LCC a GPS
		t = proj.transform(i[0],i[1])
		x = t[0]
		y = t[1]
		xy = [x,y]
#		n = (x,y)
#		coord.append(xy)
# La lista coort lo que hace es que agarra las de un polígono las mete en coord2 y se reinicia a []
		coort.append(xy)
	coord2.extend([coort])
	coort = []
#    plt.plot(x,y)
#    coord.append(shape.shape.points[:])

#Aquí lo convierte a csv
m = np.array(coord2)
#Igual aquí los prints namas fueron pa hacer pruebas, casi todos los prints que anden sueltos namas son 
#porque quería calar si si iban saliendo las cosas
#print(m)
#print(m.size)
df = pd.DataFrame(data=m)
df.to_csv('sintuplasINEGI.csv', sep=' ', header=False, index=False)

#Estas namas son pruebas que hice con print pa ver si si iban saliendo las cosas
#print(coord[0])
#print(coord2[0])
#print(coord2[1])
#print(len(coord2))

#Aquí pos namas se crea el mapa

#Crear el mapa como un objeto
#m = folium.Map(location=[19.595772, -98.997218])

#Importé el excel porque junté las coordenadas de las tiendas con las coordenadas de los AGEBS pa verlas
#from openpyxl import load_workbook

#wb = load_workbook('coordenadas.xlsx')
#sheet = wb.worksheets[0]

#coordenadas = []

#for row in sheet.iter_rows(min_row=2,values_only=True):
#	xy = [ row[0] , row[1]]
#	if xy not in coordenadas:
#		coordenadas.append(xy)

#Al FastMarkerCluster namas le das una lista con coordenadas en el primer parámetro osea la primera
#Cosa despues del ( por ejemplo en este caso la lista "coordenadas" que salió del for anterior
#Y te hace un marcador en el mapa para cada par de coordenadas y luego te los agrupa
#folium.plugins.FastMarkerCluster(coordenadas,name='Tiendas de conveniencia').add_to(m)

#Lo mismo que arriba
#folium.plugins.FastMarkerCluster(coord,name='AGEB').add_to(m)

#El collapsed=False es para que en la esquina superior derecha aparezca desde el inicio la cosa esa
#donde están las palomitas azules, si collapsed=True inicia colapsado y lo tienes que abrir haciendole click
#folium.map.LayerControl(collapsed=False).add_to(m)

#El mapa se guarda en el archivo 'completo.html' que ya te envié
#m.save('completo.html')
