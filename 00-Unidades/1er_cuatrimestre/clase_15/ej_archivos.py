lista_personas =\
[  
{
    "nombre": "Mateo",
    "apellido": "Santiago",
    "edad": 20,
    "dni": 793499999
},
{
    "nombre": "Howard",
    "apellido": "Duck",
    "edad": 35,
    "dni": 1246356443
},
{
    "nombre": "Tony",
    "apellido": "Stark",
    "edad": 40,
    "dni": 1367821390
}
]


def guardar_csv_personas(lista_personas:list, path:str):
    
    archivo = open(path, "w")
    archivo.write("nombre,apellido,edad,dni\n") #cabecera
    
    for i in range(len(lista_personas)):
        persona = lista_personas[i]
        nombre = persona["nombre"]
        apellido = persona["apellido"]
        edad = persona["edad"]
        dni = persona["dni"]
        #dni = dni.replace("\n","")
        #dni = int(dni)

        archivo.write(f"{nombre},{apellido},{edad},{dni}\n")

    archivo.close()

guardar_csv_personas(lista_personas "archivo.txt.csv")
