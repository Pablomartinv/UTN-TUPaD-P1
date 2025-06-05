#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos={}

print("Ingrese 5 contactos con sus respectivos numeros telefonicos")

for i in range(1, 6):
    nombre= input("NOMBRE: ")
    telefono= input("TELEFONO: ")
    contactos.update({nombre:telefono})

print(contactos)
