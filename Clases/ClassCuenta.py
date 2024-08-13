class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print ("Depositaste ", cantidad)

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print ("Fondos insuficientes")
        else: 
            self.balance -= cantidad
            print ("Retiraste ", cantidad)

    def saldo(self):
        print ("El cliente: ",self.titular, " Tiene un saldo de ",self.balance)

mi_cuenta = CuentaBancaria("Juan", 1000)
mi_cuenta.depositar(500)
mi_cuenta.saldo()
mi_cuenta.retirar(1000)
mi_cuenta.saldo()



