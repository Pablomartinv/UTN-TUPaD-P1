def contar_bloques(n):
    if n ==1: 
        return 1
    else:
        return n + contar_bloques(n-1)
    
base= int(input("Ingrese el numero de bloques de la base: "))
print(f"La cantidad de bloques necesarios para armar la piramide es de {contar_bloques(base)} bloques")
