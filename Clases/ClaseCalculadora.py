class Calculadora:

    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a -b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if (b ==0):
            return "Error división por cero"
        else:
            return a / b
        
calculadora = Calculadora()

print(f"La suma es: {calculadora.sumar(5,2)}")
print(f"La resta es: {calculadora.restar(5,2)}")
print(f"La multiplicación es: {calculadora.multiplicar(5,2)}")
print(f"La división es: {calculadora.dividir(6,2)}")
print(f"La división es: {calculadora.dividir(6,0)}")

