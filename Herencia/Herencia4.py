class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
 #       saludar = super().presentarse()
 #       return f"{saludar} y estudio {self.carrera}."
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

# Crear una instancia de Estudiante
estudiante = Estudiante("María", 20, "Ingeniería")
print(estudiante.presentarse())  # Salida: Hola, soy María, tengo 20 años y estudio Ingeniería.
print(estudiante.estudiar())     # Salida: María está estudiando Ingeniería.
