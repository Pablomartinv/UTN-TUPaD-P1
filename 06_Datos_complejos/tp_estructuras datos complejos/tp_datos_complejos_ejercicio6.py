print("Ingrese los nombres de los alumnos y sus respectivas notas" )

alumnos={} #se declara el diccionario vacio

for i in range(1,4):
    nombre= input(f"Nombre del {i}° alumno:  ")
    
    notas=[]

    print("Ingrese las 3 notas")
    for i in range(1,4):
        nota= float(input(f"{i}° nota: "))
        notas.append(nota)
     
    notas= tuple(notas)#se convierte la lista de notas en una tupla   

    alumnos.update({nombre:notas})#se almacenan los nombres y sus respectivas notas

print(alumnos)

for alumno, notas in alumnos.items():
    promedio= sum(notas)/len(notas)
    print(f"{alumno} tiene el promedio: {promedio}")
