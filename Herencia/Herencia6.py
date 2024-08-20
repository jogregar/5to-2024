class empleado:
    def __init__(self, salario):
        self.salario = salario
    
    def mostrarsalario (self):
        return f"el salario es: {self.salario}"
    
class gerente (empleado):
    def __init__(self, salario, bono):
        super().__init__(salario)
        self.bono = bono
        
    def mostrarsalario (self):
        salariototal = self.salario+self.bono
        return f"el salario con bono es: {salariototal}"
    
geren =  gerente(12000,3000)
print (geren.mostrarsalario())
