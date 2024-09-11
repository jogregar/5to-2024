class MetodoPago:
    def procesar_pago(self, cantidad):
        pass

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Procesando pago de {cantidad} con tarjeta de crédito."

class PayPal(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Procesando pago de {cantidad} a través de PayPal."

class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, cantidad):
        return f"Procesando pago de {cantidad} mediante transferencia bancaria."

tarjeta = TarjetaCredito()
paypal = PayPal()
transferencia = TransferenciaBancaria()

print (tarjeta.procesar_pago(10000))
print (paypal.procesar_pago(35000))
print (transferencia.procesar_pago(25000))
