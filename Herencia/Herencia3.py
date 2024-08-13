class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return (f"Empleado: {self.nombre}, Salario: {self.salario}")
    
class Gerente(Empleado):
    def __init__(self, nombre, salario,empleados_a_cargo):
        super().__init__(nombre, salario)
        self.empleados_a_cargo = empleados_a_cargo

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info}, Empleados a cargo: {self.empleados_a_cargo}")
    
gerente = Gerente("José",150000,18)
print(gerente.mostrar_informacion())
