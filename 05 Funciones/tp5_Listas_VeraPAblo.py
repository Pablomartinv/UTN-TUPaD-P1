# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

print("A continuacion se mostrara una lista con los numeros multiplos de 4 del 0 al 100")
multiplos= list(range(0,101,4))
print(multiplos)
print("\n")


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo.

lista= [True, 31552183, "Pablo", "abril", "Argentina" ]
print("La lista tiene ",len(lista), "elementos")
#podemos mostrar el valor del anteultimo elemento ingresando directamente con el numero de posicion
print("El penultimo elemento de la lista es: ",lista[3])
#o mediante la longitud y restamos las posiciones
print(lista[len(lista)-2])
print("\n")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla.

listaVacia=[]

listaVacia.append("verduras")
listaVacia.append("frutas")
listaVacia.append("cereales")
print("La lista con los nuevos elementos almacenados con el metodo appen resulta: ",listaVacia)
print("\n")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "conejo", "pez"]
print("La lista original es: ", animales)
animales[1]="loro"  #Reemplazamos el valor de la posicion 2
animales[len(animales)-1]= "oso"  #reemplazamos el valor de la ultima posicion
print("La nueva lista resulta: ", animales)
print("\n")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros= [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) #elimina el numero con el mayor valor
print(numeros)
print("\n")

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista5= list(range(10,31,5))#creamos la lista con la funcion range y los parametros inicio, fin, intervalos
print("La lista creada es:",lista5)
print("Los 2 primeros elementos son", lista5[0:2])#mostramos los 2 primeros elementos, desde la posicion 0 a la 2 que no es incluida
print("\n")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
print("La lista original es:", autos)
autos[1]= "t-cross"
autos[2]= "taos"
print("La nueva lista es:", autos)
print("\n")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles= []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print("Los valores de la lista dobles es:", dobles)
print("\n")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print("La lista origina de compras es:", compras)
# a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")
print("Al sumar el elemento jugo en el tercer cliente, resulta: ",compras)

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"
print("Al reemplazar fideos por tallarines, resulta:", compras)

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print("Al eliminar pan de la lista del primer cliente, resulta: ",compras)
print("\n")

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla

lista_anidada= []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5])
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)
print(lista_anidada)