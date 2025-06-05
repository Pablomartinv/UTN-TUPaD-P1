#ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
#se añaden los siguientes elementos al diccionario

precios_frutas["Naranja"]= 1200
precios_frutas["Manzana"]= 1500
precios_frutas["Pera"]= 2300

#ejercicio 2
#se actualizan precios 
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]= 1700
precios_frutas["Melon"]= 2800

print(precios_frutas)

#ejercicio 3
#se pide una nueva lista solamente con las frutas sin los precios

solo_frutas= precios_frutas.keys()

print("La lista con las frutas sin los precios es: ", solo_frutas)


