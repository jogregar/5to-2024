class persona:
    def __init__(self,nombre,edad):
        self.nombre= nombre 
        self.edad= edad
        
    def presentarse(self):
        return f"hola, me llamo {self.nombre} y tengo {self.edad}"
    
class Estudiante(persona):
    def __init__(self,nombre,edad,carrera):
        super().__init__(nombre,edad)
        self.carrera= carrera

    def estudiar (self):
        presentacion=super().presentarse()
        return f"{presentacion} estudio {self.carrera}"
    
estudiante=Estudiante("bacher","17","fornite")
print(estudiante.estudiar())
