class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        salario = self.salario_base + self.bono 
        return f"El Salario de {self.nombre} es de {salario}"

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_base, horas_trabajadas):
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
    
    def calcular_salario(self):
        salario = self.salario_base * self.horas_trabajadas / 40 
        return f"el salario de {self.nombre} es de {salario}"

empleado1 = EmpleadoTiempoCompleto("Ana", 30000, 5000)
empleado2 = EmpleadoMedioTiempo("Juan", 30000, 20)

print(empleado1.calcular_salario()) 
print(empleado2.calcular_salario())