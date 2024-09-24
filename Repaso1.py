class Empleado:
    def __init__(self, nombre, salario_base, bono_anual):
        self.nombre = nombre
        self.salario_base = salario_base
        self.bono_anual = bono_anual
    
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono_anual):
        super().__init__(nombre, salario_base, bono_anual)
    
    def calcular_salario(self):
        return self.salario_base + (self.bono_anual / 12)

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, salario_por_hora):
        super().__init__(nombre, salario_base=0, bono_anual=0)
        self.salario_por_hora = salario_por_hora
    
    def calcular_salario(self, horas_trabajadas):
        return self.salario_por_hora * horas_trabajadas

class Freelancer(Empleado):
    def __init__(self, nombre, pago_por_proyecto):
        super().__init__(nombre, salario_base=0, bono_anual=0)
        self.pago_por_proyecto = pago_por_proyecto
    
    def calcular_salario(self):
        return self.pago_por_proyecto

# #Lista de empleados en una tupla usando polimorfismo
# empleados = [
#     EmpleadoTiempoCompleto("Carlos", 3000, 1200),
#     EmpleadoTiempoParcial("Ana", 50),
#     Freelancer("Pedro", 5000)
# ]

# # Recorremos la tupla y calculando los salarios usando polimorfismo
# for empleado in empleados:
#     if isinstance(empleado, EmpleadoTiempoParcial): #Verificamos si en mi objeto existe EmplezdoTiempoParcial
#         salario = empleado.calcular_salario(80)
#     else:
#         salario = empleado.calcular_salario()
    
#     print(f"Empleado: {empleado.nombre}, Salario mensual: ${salario}")

Completo = EmpleadoTiempoCompleto("Carlos", 3000, 1200)
Parcial = EmpleadoTiempoParcial("Ana", 50)
Libre = Freelancer("Pedro", 5000)

print (f"Empleado Tiempo Completo: {Completo.nombre}, Salario: {Completo.calcular_salario()}")
print (f"Empleado Tiempo Parcial: {Parcial.nombre}, Salario: {Parcial.calcular_salario(80)}")
print (f"Empleado Libre: {Libre.nombre}, Salario: {Libre.calcular_salario()}")