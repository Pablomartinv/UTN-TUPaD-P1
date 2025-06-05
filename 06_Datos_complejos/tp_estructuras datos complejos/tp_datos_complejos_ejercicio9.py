agenda={
    ("Lunes", "10:00"):"reunion",
    ("Martes", "15:00"): "clases de ingles",
    ("Miercoles", "18:30"): "natacion",
    ("Lunes", "12:00"):"almuerzo laboral"
}


print("desea consultar la agenda?")
print("Ingrese dia y hora para saber que actividad esta agendada")
consulta_dia= input("Dia: ")
consulta_hora= input("Hora: ")

for k,v in agenda.items(): 
    if consulta_dia == k[0] and consulta_hora == k[1] :
        print("El evento agendado es: ", v)




