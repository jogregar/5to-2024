
class MetodoPago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Debes implementar el método procesar_pago en la clase derivada")

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se está pagando ${monto} con Tarjeta de Crédito"

class Paypal(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se está pagando ${monto} con Paypal"

class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se está pagando ${monto} con Transferencia Bancaria"

tarjeta_credito = TarjetaCredito()
paypal = Paypal()
transferencia_bancaria = TransferenciaBancaria()

monto = 100
print(tarjeta_credito.procesar_pago(monto)) 
print(paypal.procesar_pago(monto)) 
print(transferencia_bancaria.procesar_pago(monto)) 