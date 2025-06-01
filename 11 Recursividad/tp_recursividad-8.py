
def contar_digito(num, dig):
    if num ==0:
        return 0    
    elif (num%10)== dig:         
         return 1+contar_digito(num //10, dig)
    else:
        return contar_digito(num //10, dig)

print("Ingrese un numero entero positivo y un digito. Se mostrará cuantas veces aparece el digito ingresado en el numero")
num= int(input("numero: "))
dig= int(input("Digito: "))
print(f"El digito {dig} aparece {contar_digito(num, dig)} veces en el numero {num}")