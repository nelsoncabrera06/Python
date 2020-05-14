import numpy
import matplotlib.pyplot as plt
import json 

# quiero aplicar machine learning al BITCON
#f = open('market-price-all.json') # el json de BITCOIN
f = open('oro_mensual.json') # el json de BITCOIN
data = json.load(f)

print("Encabezados:")
for x in data:
  print(x)
print("")
# declaro la lista 
x = []  # aca voy a tener el tiempo en formato int (unix timestamp)
y = []  # aca voy a tener el precio en dolares
labels = []

for i in data['values']:
  x.append(i['x'])
  y.append(i['y'])
#print(x[300]) #1308700800
#print(len(x)) #1383
# ya estan los datos cargados
# ahora tengo que Split Data, dividir los datos en training, validacion, test
# mi proporcion elegida es training 70% - test %30
# el 70% de 1383 es 968,1 ~ 968
# el 30% de 1383 es 414,9 ~ 415
training = round(len(x) * 0.7)  # round hace una aproximacion
test = round(len(x) * 0.3)      # round redondea
print(training) #968 estan bien divididos

entrenamiento = [] 
prueba = []  
validacion = []
"""
for i in data['values']:
  x.append(i['x'])
  y.append(i['y'])
"""
#unix timestamp # transformo un int en tiempo
from datetime import datetime
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
mymodel = numpy.poly1d(numpy.polyfit(x, y, 12)) #(x, y, grado del polinimio)
fin = x[-1]+10000000
myline = numpy.linspace(x[0], fin, 100) # (inicio, fin, n° de muestras a generar)
print("ultima prediccion {} ---- Dolares: {:.2f}".format(datetime.utcfromtimestamp(fin).strftime('%H:%M:%S %d-%m-%Y'),mymodel(fin)))

pasos = len(labels_unicos)
intervalo = len(x) / pasos
ejex = []
for i in range(pasos):
    ejex.append(x[i*int(intervalo)])
 
fig, ax = plt.subplots()
ax.set_xlabel('Bitcoin')
ax.set_ylabel('Precio en Dolares')
plt.grid(color='0.95')

#plt.scatter(x, y, marker='o', label='first', s=2.5)#, color='#1f77b4') # esta funcion pone puntos
plt.plot(x, y, label='datos') #, color='#1f77b4') # esta funcion dibuja lineas
plt.plot(myline, mymodel(myline), c='r', label='modelizado')

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