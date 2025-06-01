def facto(n):
    if n <=1:
        return 1
    else:
        return n * facto(n-1)
    
numero= int(input("Ingrese un numero y se mostrara el factorial de cada uno de los numeros que le preceden: "))
for i in range(1,numero+1):
        print(f"El factorial del numero {i} es: {facto(i)}")
    
