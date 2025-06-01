def es_palindromo(palabra):
    if len(palabra)<=1:
        print("Es palindromo")
    elif palabra[0] != palabra[-1]:
        print("No es palindromo")
    else:
        palabra=palabra[1:-1]
        es_palindromo(palabra)

es_palindromo("ahora")
