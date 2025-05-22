import math

# #se definen las funciones

# #ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!!!")


# #ejercicio 2
def saludar_usuario(nombre):
   print(f"Hola {nombre}!")


# #ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# #ejercicio 4
def calcular_area_circulo(radio):    
    return math.pi*(radio**2)

def calcular_perimetro_circulo(radio):
    return 2*math.pi*radio

# #ejercicio 5
def segundos_a_horas(segundos):
    return segundos/3600


# #ejercicio 6
def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado= numero*i
        print(f"{numero} X {i} = {resultado}")

#ejercicio 7
def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    multi=a*b
    div=a/b
    tupla=(suma, resta, multi, div)
    print(tupla)


#ejercicio 8
def calcular_imc(peso, altura):
    imc= peso/(altura**2)
    return imc

#ejercicio 9
def celsius_a_fahrenheit(celsius):
    far= celsius*1.8+32
    return far

#ejercicio 10
def calcular_promedio(a, b, c):
    return (a+b+c)/3


#<----------------------------------------------------------------->
#se invoca a las funciones desde el programa principal

#ejercicio 1
imprimir_hola_mundo()

# #ejercicio 2
nombre= input("Ingrese su nombre: ")
saludar_usuario(nombre)

# #ejercicio 3
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= input("Ingrese su edad: ")
residencia= input("Ingrese la ciudad en la cual reside: ")
informacion_personal(nombre, apellido, edad, residencia)


# #ejercicio 4
radio= float(input("Ingrese el radio del circulo en centimetros: "))
print(f"El area del circulo es {calcular_area_circulo(radio)} centimetros")
print(f"El perimetro del circulo es {calcular_perimetro_circulo(radio)} centimetros")


# #ejercicio 5
segundos=float(input("Ingrese los segundos para convertirlos en horas: "))
print(f"Los segundos ingresados equivalen a {segundos_a_horas(segundos)} horas")

#ejercicio 6
numero= int(input("Ingrese un numero entero para visualizar su tabla de multiplicar: "))
while numero <= 0:
    print("Error. Debe inhgresar un numero entero mayor a 0")
    numero= int(input("Ingrese numero: "))
tabla_multiplicar(numero)

#ejercicio 7
print("Ingrese dos numeros para realizar las operaciones de suma, resta, multiplicacion y division")
num1= int(input("numero 1: "))
num2= int(input("numero 2: "))
operaciones_basicas(num1, num2)


#ejercicio 8
print("Ingrese su peso expresado en kilogramos y su altura expresada en metros")
peso= float(input("peso en kg: "))
altura= float(input("altura en metros: "))
print(f"Su indice de masa corporal es de {round(calcular_imc(peso, altura),2)}")  

#ejercicio 9
print("Ingrese la temperatura expresada en gracos Celsius para ver su equivalente en Fahrenheit")
celsius= float(input("grados °C: "))
fahr= celsius_a_fahrenheit(celsius)
print(f"La tempreratura ingresada es de {fahr} ° F")

#ejercicio 10
print("Ingrese 3 numeros para saber su promedio")
n1= float(input("1er numero: "))
n2= float(input("2do numero: "))
n3= float(input("3er numero: "))
print(f"El promedio de los tres numeros ingresados es {calcular_promedio(n1, n2, n3)}")
