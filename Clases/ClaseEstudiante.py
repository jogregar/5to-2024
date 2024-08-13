

class Estudiantes:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []

    def mostrar_datos(self):
        print(self.nombre, " ", self.apellido)

    def mostrar_notas(self):
        print(self.notas)  
        for nota in self.notas:
            print (nota)
           

    def agregarnota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        print("El promedio de notas es: ", sum(self.notas)/len(self.notas))

    def __str__(self):
        return (f"El promedio de notas del estudiante es {sum(self.notas)/len(self.notas)}")
        # return str(sum(self.notas)/len(self.notas))

estudiante1 = Estudiantes("Pedro", "Perez")
estudiante1.mostrar_datos()
estudiante1.agregarnota(8)
estudiante1.agregarnota(5)
estudiante1.agregarnota(6)
estudiante1.agregarnota(1)
estudiante1.mostrar_notas()
print(estudiante1)
estudiante1.promedio() 
estudiante1.agregarnota(10)
estudiante1.promedio() 



