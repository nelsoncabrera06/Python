import numpy
import matplotlib.pyplot as plt
import json 
import re
# quiero aplicar machine learning al ORO
# https://datahub.io/core/gold-prices
#f = open('market-price-all.json') # el json de BITCOIN
f = open('oro_mensual.json') # el json de BITCOIN
data = json.load(f)
#print(type(data))  # es una lista
#print(len(data))   # de 844 elementos
#print(data[0])     # {'Date': '1950-01', 'Price': 34.73}
#print(type(data[0]))    # tipo dict
#print(data[0]['Date'])     # 1950-01
#print(data[0]['Price'])     # 34.73

# declaro la lista 
x = []  # aca voy a tener el tiempo en formato int (unix timestamp)
y = []  # aca voy a tener el precio en dolares
labels = []

for i in data:
  x.append(i['Date'])
  y.append(i['Price'])
print("")

#labels = x.copy()
#print(len(labels)) # 844 ok

#print(x[0]) # 1950-01 esto esta bien el problema es con los labels
#print(y[0]) # 34.73

#print(x[300]) # 1975-01 año y mes
#print(len(x)) # 844 elementos ok!
# ya estan los datos cargados
# ahora tengo que Split Data, dividir los datos en training, validacion, test
# mi proporcion elegida es training 70% - test %30
# el 70% de 1383 es 968,1 ~ 968
# el 30% de 1383 es 414,9 ~ 415
training = round(len(x) * 0.7)  # round hace una aproximacion
test = round(len(x) * 0.3)      # round redondea
print(training)         #591 estan bien divididos

entrenamiento = [] 
prueba = []  
validacion = []

#unix timestamp # transformo un int en tiempo # en este caso no es necesario
from datetime import datetime
"""for i in x:
    #labels.append(datetime.utcfromtimestamp(i).strftime('%H:%M:%S %d-%m-%Y'))
    labels.append(datetime.utcfromtimestamp(i).strftime('%Y'))
"""
for i in x:
    labels.append(re.findall(r"^\d+", i)[0])   # copio solo los años

#print(labels) # ahora esta bien tengo una lista de fechas
#print(type(labels)) # tipo list
print("largo de labels {}".format(len(labels))) # 844

#year = re.findall(r"^\d+", labels[0]) # extraigo solo el año
#print (year) # ['1950']

#print (type(labels))    # <class 'list'>

def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    #return list(uniq(sorted(l, reverse=True)))
    return list(uniq(sorted(l, reverse=False)))

labels_unicos = sort_and_deduplicate(labels)

new_labels = [None] * len(labels)
rango = range(1, len(labels), 20)
for n in rango:
  new_labels[n] = labels[n] 

#print("Lista de new numbers : ", new_labels) # parece q esta bien


# lista con valores unicos
"""my_set = set(labels)
labels_unicos = list(my_set)
labels_unicos.sort()"""
print("largo de new labels {}".format(len(new_labels)))   # mismo largo 844 pero con muchos vacios
#print("List of new labels : ", new_labels) # se lo ve bien

print(x[0]) # 1950-01 tipo str
print(y[0]) # 34.73 tipo float
# mi linea - Polynomial Regression
mymodel = numpy.poly1d(numpy.polyfit(range(len(x)), y, 5)) #(x, y, grado del polinimio)
inicio = 0 # x[0]
fin = len(x) #+ 10000000
myline = numpy.linspace(inicio, fin, 100) # (inicio, fin, n° de muestras a generar)
print("ultima prediccion {} ---- Dolares: {:.2f}".format(datetime.utcfromtimestamp(fin).strftime('%H:%M:%S %d-%m-%Y'),mymodel(fin)))

#pasos = len(labels_unicos)
pasos = len(new_labels)
intervalo = len(x) / pasos
ejex = []
for i in range(pasos):
    ejex.append(x[i*int(intervalo)])
 
fig, ax = plt.subplots()
ax.set_xlabel('Oro')
ax.set_ylabel('USD/kg', rotation=0, labelpad=20)
#plt.grid(color='0.95')

#plt.scatter(x, y, marker='o', label='first', s=2.5)#, color='#1f77b4') # esta funcion pone puntos
plt.plot(x, y, label='datos') #, color='#1f77b4') # esta funcion dibuja lineas
plt.plot(myline, mymodel(myline), c='r', label='modelizado')

# You can specify a rotation for the tick labels in degrees or with keywords.
#plt.xticks(x,labels_unicos, rotation='vertical')
#plt.xticks(ejex, labels_unicos, rotation='45')
#plt.xticks(ejex, new_labels, rotation='45')
plt.xticks(range(len(x)), new_labels, rotation='45')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)

plt.show()

# Closing file 
f.close() 