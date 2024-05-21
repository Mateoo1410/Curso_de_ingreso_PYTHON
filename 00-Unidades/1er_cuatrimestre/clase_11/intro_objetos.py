class alumno: #class para crear el objeto y ponerle nombre

    especie = "Humano"   #se pone de esta forma para que sean todos Humanos por defecto(atributo de clase)
    def __init__(self, nombre:str, apellido:str, DNI:int, contrasenia:str): #CLASE/INFO(atributos de instancia)
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.contrasenia = contrasenia #asi ya que la ñ no esta en el alfabeto estadounidense
    
    def presentarse(self, saludo_final:str)->str:   #METODO/ACCION
        return f"Hola a todos mi nombre es {self.nombre} mi apellido es {self.apellido}  y mi DNI de yapa epresentarse {self.DNI}. {saludo_final}"

alumno_1 = alumno("Mateo", "Santiago", 123456789, "123")
alumno_2 = alumno("Juan", "Perez", 1000000, "321")

print(alumno_1.presentarse("Chau nos vemos"))
print(alumno_2.presentarse("Que les vaya bien"))

#self para que dentro de el se le agreguen clases y sepa donde se esta creando el objeto(es el molde para crear personajes/objetos)