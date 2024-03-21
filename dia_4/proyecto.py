#crear una clase persona que tenga como atributos nombre, edad y pais de origen
#crear un metodo que imprima el nombre de la persona
#crear un metodo que imprima la edad de la persona
#crear un metodo que imprima el pais de origen de la persona
#crear un metodo que imprima todos los datos de la persona
#crear una instancia de la clase persona


class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_edad(self):
        print(self.edad)

    def imprimir_pais(self):
        print(self.pais)

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Pais: {self.pais}")
    
persona = Persona("Juan", 25, "Mexico")

#crear una clase llamada estudiante que herede de la clase persona
#crear un metodo que imprima el nombre del estudiante
#crear un metodo que imprima la edad del estudiante
#crear un metodo que imprima el pais de origen del estudiante
#crear un metodo que imprima todos los datos del estudiante
#crear una instancia de la clase estudiante

class Estudiante(Persona):
    def __init__(self, nombre, edad, pais, matricula):
        super().__init__(nombre, edad, pais)
        self.matricula = matricula

    def imprimir_matricula(self):
        print(self.matricula)
        
