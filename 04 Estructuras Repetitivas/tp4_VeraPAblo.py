# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("A continuacion vera una lista de los numeros enteros desde el 0 hasta el 100")
for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num= input("ingrese un numero entero ")
while not num.isdigit(): #validacion que la entrada realizada por el usuario sea un numero.
    print("ERROR. Debe ingresar un numero")
    num= input("ingrese un numero entero ")  
long= len(num) #se lee la longitud de la cadena para saber las cifras del numero.     
print(f"El numero ingresado tiene {long} digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Ingrese dos numeros enteros")
num1= input("primer numero: ")
num2= input("segundo numero: ")

while not num1.isdigit() or not num2.isdigit():#valida que los ingresos sean numeros
    print("ERROR. debe ingresar 2 numeros enteros positivos. Intente nuevamente")
    num1= input("primer numero: ")#se vuelve a pedir el ingreso de numeros 
    num2= input("segundo numero: ")
num1= int(num1)#se convierten a numero    
num2= int(num2)
sumatoria=0
for i in range(num1+1, num2):#se realiza la suma de los numeros comprendidos en el rango dado
    sumatoria= sumatoria+i
    
print(f"La sumatoria de los numeros comprendidos en el rango dado por los numeros ingresados es de {sumatoria}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero= int(input("Ingrese un numero entero para ser sumado. Para finalizar ingrese 0  "))
suma =0
while numero !=0:
    numero= int(numero)
    suma= suma + numero
    numero= int(input("Ingrese otro numero entero para ser sumado, de lo contrario, ingrese 0 para finalizar  "))

print("La suma de todos los numeros ingresados es de ", suma)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
cont=1
numero_secreto= random.randint(0,9)
print("Adivine el numero aleatorio del 0 al 9")
adivina_numero= int(input())
while adivina_numero != numero_secreto:
    adivina_numero= int(input("Intente de nuevo. Ingrese un numero del 0 al 9 "))
    cont+=1
print(f"Felicitaciones, adivino el numero secreto en {cont} intentos")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

print("A continuacion vera una lista de los numeros pares comprendidos entre el 0 y el 100, en orden decreciente")
for i in range(100, 0-1, -2):
    print(i, end="  ")


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("Ingrese un numero, se mostrara la sumatoria de todos los numeros comprendidos entre 0 y su ingreso")
num= input()
suma=0
while not num.isdigit():#se valida que el ingreso sea un numero
    num= input("Debe ingresar un numero entero, pruebe nuevamente  ")    

num=int(num)#se convierte el ingreso a numero
for i in range(1,num+1):
    print(i,end="+")
    suma= suma + i
print("\n")
print("La suma de los numeros comprendidos en el rango dado resulta ser: ", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad=5 # a cambiamos esta variable para aumentar el numero de ingresos por parte del usuario
print(f"Debe ingresar {cantidad} numeros a su eleccion")
pares=0
impares=0
pos=0
neg=0
for i in range (1, cantidad+1):
    num= int(input( "Ingrese su numero "))
    if num % 2 ==0:
        pares=pares+1
    else:
        impares= impares+1
    if num >= 0 :
        pos+=1
    else:
        neg+=1   
print("Dentro de los numeros ingresados habia: ")        
print(f"{pares} numero pares y {impares} numeros impares")
print(f"{pos} numeros positivos y {neg} numeros negativos")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cant= 5#esta variable se cambia por un valor mayor cuando se lo requiera
suma=0
print(f"Debe ingresar {cant} numeros a su eleccion")
for i in range (1, cant+1):#se ingresan los numeros y se acumula la suma de los mismos
    print(f"Ingrese el {i}° numero ")
    numer= int(input())
    suma+=numer
print(f"La media de los {cant} numeros ingresados es: {suma/cant} ")
