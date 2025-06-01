def fibo(posicion):
    if posicion == 0:
        return 0
    elif posicion ==1:
        return 1
    else:
        return fibo(posicion -1)+fibo(posicion-2)
    
p=int(input("Indique que posicion de la serie Fibbonacci desea ver: "))
for i in range(0, p+1):
    print(f"La posicion {i} de la serie Fibonacci corresponde al numero: {fibo(i)}")