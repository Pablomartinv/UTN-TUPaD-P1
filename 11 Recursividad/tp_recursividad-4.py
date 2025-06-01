def decimalAbinario(decimal):
    if decimal==0:
        return "0"
    elif decimal==1:
        return "1"
    else:        
        return decimalAbinario(decimal//2)+ str(decimal%2)


numero= int(input("Ingrese un numero para convertirlo a binario: "))
print(f"el numero {numero} convertifo a binario es: {decimalAbinario(numero)}")