def potencia(base, exponente):
    if exponente== 0:
        return 1
    elif base ==0:
        return 0
    elif exponente==1:
        return base
    else:
         return base * potencia(base, exponente-1)

print(potencia(2,4))