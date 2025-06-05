frase= input("ingrese una frase ")
#convierte la frase ingresada en una lista con las palabras
frase= frase.split()

for i in range(len(frase)):
    frase[i]= frase[i].lower()#se transforman todas las palabras con sus letras a minusculas

frecuencia={}
for palabra in frase:
    if palabra in frecuencia:
        frecuencia[palabra]+=1
    else:
        frecuencia[palabra]=1

#se convierte a set la lista, para que no devuelva elementos repetidos
frase_set= set(frase)

print("Las palabras utilizadas en la frase ingresada son: ", frase_set)
print("La frecuencia de cada palabra es: ", frecuencia)



    


