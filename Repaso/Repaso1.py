class Empleado:
    def __init__(self,nombre,salario_base,bono_anual):
        self.nombre = nombre
        self.salario_base = salario_base
        self.bono_anual = bono_anual
    def calcular_salario(self):
        pass


class Empleado_tiempo_completo(Empleado):
    def __init__(self,nombre,salario_base,bono_anual):
        super().__init__(nombre,salario_base,bono_anual)
    def calcular_salario(self):
        return (self.salario_base + self.bono_anual / 12)

class Empleado_tiempo_parcial(Empleado):
    def __init__(self,nombre,pago_por_horas):
        self.pago_por_horas = pago_por_horas
        super().__init__(nombre,salario_base=0,bono_anual=0)
    def calcular_salario(self,horas_trabajadas):
        return (horas_trabajadas*self.pago_por_horas)

class Freelancer(Empleado):
    def __init__(self,nombre,pago_fijo):
        self.pago_fijo = pago_fijo
        super().__init__(nombre,salario_base=0,bono_anual=0)
    def calcular_salario(self):
        return (self.pago_fijo)
    
empleado_tiempo_completo = Empleado_tiempo_completo("Augusto",100000,50000)
empleado_tiempo_parcial = Empleado_tiempo_parcial("Maximo",100)
freelancer = Freelancer("Jose",500)

print(f"empleado tiempo completo: {empleado_tiempo_completo.nombre},sueldo: {empleado_tiempo_completo.calcular_salario()}")
print(f"empleado tiempo parcial: {empleado_tiempo_parcial.nombre}, sueldo: {empleado_tiempo_parcial.calcular_salario(40)}")
print(f"empleado freelancer: {freelancer.nombre}, sueldo: {freelancer.calcular_salario()}")
    