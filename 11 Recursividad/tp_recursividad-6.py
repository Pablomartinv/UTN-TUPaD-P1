
def suma_digitos(num):  
    if num ==0:
        return num
    else:
        return num%10 +suma_digitos(num//10)
    

numero= int(input("Ingrese un numero entero positivo para saber el valor de la suma de sus digitos: "))
print(suma_digitos(numero))