# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad= int((input("Ingrese su edad: ")))
# if edad > 18:
#     print("Es mayor de edad")

#---------------------------------------------------------------------------------------------------
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota= int(input("Ingrese su nota: "))
# if nota >= 6:
#     print("APROBADO")
# else:
#     print("DESAPROBADO")    

#---------------------------------------------------------------------------------------------------
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero= int(input("Ingrese un numero: "))
# if numero % 2 ==0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")    

#---------------------------------------------------------------------------------------------------
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese por favor su edad: "))
# if edad < 12:
#     print("Usted pertenece a la categoria niño/a")
# elif edad < 18:
#     print("Usted corresponde a la categoria adolescente")
# elif edad < 30:
#     print("Usted pertenece a la categoria Adulto/a joven")
# else:
#     print("Usted pertenece a la categoria Adulto/a")      

#---------------------------------------------------------------------------------------------------
# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".     

# contrasenia= input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# longitud = len(contrasenia)
# if longitud >= 8 and longitud <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")  
 
#--------------------------------------------------------------------------------------------------- 
# 6)Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# from statistics import mode, median, mean
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)

# print("La media de la lista de numeros es: ", media)
# print("La mediana de la lista de numeros es: ", mediana)
# print("La moda de la lista de numeros es: ", moda)

# if media > mediana and mediana > moda:
#     print("Hay sesgo positivo")
# elif media < mediana and mediana < moda:
#     print("Hay sesgo negativo")
# elif media == mediana and mediana == moda:
#     print("No hay sesgo")
    
#------------------------------------------------------------------------------------------------
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# cadena= input("Ingrese una palabra o frase: ")
# cadena =cadena.lower()
# long= len(cadena)
# if cadena[long-1] == "a" or cadena[long-1]=="e" or cadena[long-1]== "i" or cadena[long-1]== "o" or cadena[long-1]=="u":
#     print(cadena +"!")
# else:
#     print(cadena)


#------------------------------------------------------------------------------------------------
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

# nombre= input("Ingrese su nombre: ")
# print("Ingrese 1 si quiere su nombre en MAYUSCULAS")
# print("Ingrese 2 si quiere su nombre en minusculas")
# print("Ingrese 3 si quiere su nombre con la primer letra en MAYUSCULA")
# opcion= input("opcion: ")

# if opcion == "1" :
#     print(nombre.upper()) 
# elif opcion == "2":
#     print(nombre.lower())
# else:
#     print(nombre.title())    


#------------------------------------------------------------------------------------------------
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

# magnitud= float(input("Ingrese la magnitud del terremoto registrada, valores enteros y/o decimales entre 0 y 10: "))
# if magnitud < 3:
#     print("Magnitud en la escala de Richter: MUY LEVE, IMPERCEPTIBLE")
# elif magnitud < 4:
#     print("Magnitud en la escala de Richter: LEVE, LIGERAMENTE PRECEPTIBLE")    
# elif magnitud < 5:
#     print("Magnitud en la escala de Richter: MODERADO, PUEDE PERCIBIRSE PERO NO CAUSAR DAÑOS")
# elif magnitud < 6:
#     print("Magnitud en la escala de Richter: FUERTE, PUEDE CAUSAR DAÑOS")
# elif magnitud < 7:
#     print("Magnitud en la escala de Richter: MUY FUERTE, PUEDE CAUSAR DAÑOS SIGNIFICATIVOS")
# else:
#     print("Magnitud en la escala de Richter: EXTREMO, PUEDE CAUSAR DAÑOS A GRAN ESCALA")


#------------------------------------------------------------------------------------------------
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


print("Ingrese en que hemisferio se encuentra: ")
hemisferio= input("Hemisferio norte ingrese N, para hemisferio sur ingrese S ")
hemisferio = hemisferio.upper()
mes = input("Ingrese en que mes del año se encuentra: enero, febrero, marzo..etc. ")
mes = mes.lower()
dia= int(input("Ingrese en que dia del mes se encuentra: 1, 2, 3.. etc"))
# validacion de la fecha
if dia < 1 :
    print("Debe ingresar un numero mayor a 0 para la fecha/dia")
elif hemisferio =="S":
    if (mes == "diciembre" and (dia >= 21 and dia <=31)) or (mes == "enero" and dia <=31) or (mes == "febrero" and dia <=28) or (mes == "marzo" and dia < 21):
        print("Usted se encuentra en la estacion VERANO")
    elif (mes=="marzo" and dia <=31) or (mes =="abril" and dia <=30) or (mes == "mayo" and dia <= 31) or (mes=="junio" and dia <21):
        print("Usted se encentra en la estacion OTOÑO")
    elif (mes =="junio" and dia <= 30) or ((mes =="julio" or mes == "agosto") and dia <=31) or (mes=="septiembre" and dia <21):
        print("Usted se encuentra en la estacion INVIERNO")
    elif (mes =="septiembre" and dia <=31) or (mes=="octubre" and dia <=31) or (mes =="noviembre" and dia <=30) or (mes =="diciembre" and dia <21):
        print("Usted se encuentra en la estacion PRIMAVERA")
    else:
        print("ERROR:verifique los datos ingresados")
elif hemisferio == "N":
    if (mes == "diciembre" and (dia >= 21 and dia <=31)) or (mes == "enero" and dia <=31) or (mes == "febrero" and dia <=28) or (mes == "marzo" and dia < 21):
        print("Usted se encuentra en la estacion INVIERNO")
    elif (mes=="marzo" and dia <=31) or (mes =="abril" and dia <=30) or (mes == "mayo" and dia <= 31) or (mes=="junio" and dia <21):
        print("Usted se encentra en la estacion PRIMAVERA")
    elif (mes =="junio" and dia <= 30) or ((mes =="julio" or mes == "agosto") and dia <=31) or (mes=="septiembre" and dia <21):
        print("Usted se encuentra en la estacion VERANO")
    elif (mes =="septiembre" and dia <=31) or (mes=="octubre" and dia <=31) or (mes =="noviembre" and dia <=30) or (mes =="diciembre" and dia <21):
        print("Usted se encuentra en la estacion OTOÑO") 
    else:
        print("ERROR:verifique los datos ingresados")    
else:
    print("Datos incorrectos")       
