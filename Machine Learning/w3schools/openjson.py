import matplotlib.pyplot as plt
# Python program to read 
# json file 
import json 

# Opening JSON file 
#f = open('data.json',) 
f = open('market-price.json',) # el json de BITCOIN

# returns JSON object as 
# a dictionary 
data = json.load(f) 

print("Encabezados:")
# print(type(data)) # data es un diccionario
for x in data:
  print(x)
print("")

#print(type(data['values'])) # data['values'] es un list
#print(len(data['values']))  # data['values'] es un lista de 1383
#print(type(data['values'][0])) # data['values'][index] es un dict
#print(data['values'][0]['x']) # data['values'] es un int
#print(data['values'][0]['y']) # data['values'] es un int

# list is declared 
x = []
y = []

#print("values:")
# thislist.append("orange") # agrega un elemento al final
# mylist = thislist.copy()  # copia una lista entera
for i in data['values']:
  x.append(i['x'])
  y.append(i['y'])

#  print(i)
print("")
# Iterating through the json 
# list 
"""
for i in data['values']: 
	print(i) """

#print(type(x))   # list
#print(type(y))   # list

#plt.scatter(x, y) # grafica y(x) 
plt.scatter(x, y, marker='o', label='first', s=2.5)#, color='#1f77b4')
#plt.plot(myline, mymodel(myline))
plt.show()

# Closing file 
f.close() 

