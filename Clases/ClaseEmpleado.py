class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre 
        self.puesto = puesto
        self.salario = salario

    def aumentar_salario(self, por):
        self.salario += self.salario * por /100

    def __str__(self):
        return (f"El empleado {self.nombre} que ocupa el puesto {self.puesto} tiene un nuevo salario de {self.salario:.2f}")
    
empleado = Empleado("José", "Docente", 40000)
empleado.aumentar_salario(50)
print(empleado)
