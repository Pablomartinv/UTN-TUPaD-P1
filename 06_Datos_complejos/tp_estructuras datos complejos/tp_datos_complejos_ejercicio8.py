productos={
    "remeras":50,
    "pantalones":100,
    "camperas":90,
    "shorts":60
}

print("De cual producto desea saber el stock? ")
producto= input("producto: ")

if producto in productos:
    print("El stock del producto seleccionado es: ", productos[producto])
    sumarUnidad= input("Desea agregar unidades al stock? Ingrese SI/NO")
    sumarUnidad= sumarUnidad.upper()
    if sumarUnidad == "SI":
        cant= int(input("Cuantas unidades desea agregar? "))
        productos[producto]+= cant
else:
    print("el producto consultado no existe, desea agregarlo como nuevo producto? ")    
    agregarProd= input("SI/NO: ")
    agregarProd= agregarProd.upper()
    if agregarProd == "SI":
        cant= int(input(f"Ingrese el stock del nuevo producto: {producto} "))
        productos.update({producto:cant})
    
print(productos)
