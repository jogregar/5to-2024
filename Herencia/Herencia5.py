class cuenta_bancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        return f"depositó: {monto}, saldo: {self.saldo}"

    def retirar(self, retiro):
        if (self.saldo >= retiro):
            self.saldo -= retiro
            return f"retiró: {retiro}, saldo: {self.saldo}"
        return "saldo insuficiente"
    
class cuenta_de_ahorro(cuenta_bancaria):
    def intereses(self, interes):
        self.saldo = self.saldo*(1+(interes/100))
        return f"nuevo saldo: {self.saldo:.2f}"
    
cuenta_banco = cuenta_de_ahorro(8500)
print (cuenta_banco.depositar(3000))
print (cuenta_banco.retirar(15000))
print (cuenta_banco.intereses(10))