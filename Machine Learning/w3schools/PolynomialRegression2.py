import numpy
import matplotlib.pyplot as plt
import json 
# quiero hacer regression polineal para el json de BITCO
f = open('market-price.json',) # el json de BITCOIN
data = json.load(f) 
print("Encabezados:")
for x in data:
  print(x)
print("")
# declaro la lista 
x = []
y = []
labels = []

for i in data['values']:
  x.append(i['x'])
  y.append(i['y'])
#print(x[300]) #1308700800


#unix timestamp # transformo un int en tiempo
from datetime import datetime
"""ts = x[300] #int("1284101485")
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
tiempo = datetime.utcfromtimestamp(ts).strftime('%S:%M:%H %d-%m-%Y')
print(tiempo)
print(type(tiempo))"""

#print(len(x)) # 1383
#print(x)
for i in x:
    #labels.append(datetime.utcfromtimestamp(i).strftime('%H:%M:%S %d-%m-%Y'))
    labels.append(datetime.utcfromtimestamp(i).strftime('%Y'))

#print(labels) # ahora esta bien tengo una lista de fechas
#print(type(labels)) # tipo list
print("largo de labels {}".format(len(labels))) # 1383

# lista con valores unicos
my_set = set(labels)
labels_unicos = list(my_set)
labels_unicos.sort()
print("largo de labels unicos {}".format(len(labels_unicos))) # 137
print("List of unique numbers : ", labels_unicos)


# mi linea - Polynomial Regression
mymodel = numpy.poly1d(numpy.polyfit(x, y, 8)) #(x, y, grado del polinimio)
fin = x[-1]+10000000
myline = numpy.linspace(x[0], fin, 100) # (inicio, fin, n° de muestras a generar)
print("ultima prediccion {}".format(datetime.utcfromtimestamp(fin).strftime('%H:%M:%S %d-%m-%Y')))
#

"""x_inicio = x[0]
x_fin = x[-1]
x_diferencia = x_fin - x_inicio"""
pasos = len(labels_unicos)
intervalo = len(x) / pasos
ejex = []
for i in range(pasos):
    ejex.append(x[i*int(intervalo)])
  #ejex[i] = ejex[i-1] + intervalo
  #print(i) # perfecto i es el indice

#fig, ax = plt.subplots(constrained_layout=True)
fig, ax = plt.subplots()
ax.set_xlabel('Bitcoin')
ax.set_ylabel('Precio en Dolares')
plt.grid(color='0.95')
#plt.grid(color='0.95', linestyle='-', linewidth=2)

plt.scatter(x, y, marker='o', label='first', s=2.5)#, color='#1f77b4')
plt.plot(myline, mymodel(myline), c='r')

# You can specify a rotation for the tick labels in degrees or with keywords.
#plt.xticks(x,labels_unicos, rotation='vertical')
plt.xticks(ejex, labels_unicos, rotation='45')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)


plt.show()

# Closing file 
f.close() 

