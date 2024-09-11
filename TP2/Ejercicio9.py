class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        pass

class Profesor(Persona):
    def presentarse(self):
        return f"Soy el profesor {self.nombre}, tengo {self.edad} años."

class Estudiante(Persona):
    def presentarse(self):
        return f"Soy el estudiante {self.nombre}, tengo {self.edad} años."

class Administrador(Persona):
    def presentarse(self):
        return f"Soy el administrador {self.nombre}, tengo {self.edad} años."

def mostrar_informacion(datos):
    for mostrar in datos:
        print (mostrar.presentarse())

# profesor = Profesor("Carlos", 40)
# estudiante = Estudiante("María", 20)
# administrador = Administrador("Luis", 35)

# print(profesor.presentarse())
# print(estudiante.presentarse())
# print(administrador.presentarse())

datos = [Profesor("Carlos", 40), Estudiante("María", 20), Administrador("Luis", 35) ]
mostrar_informacion(datos)