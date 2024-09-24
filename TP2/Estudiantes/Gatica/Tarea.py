7.
# Clase base Publicación
class Publicacion:
    def mostrar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada Texto
class Texto(Publicacion):
    def mostrar(self):
        return "Publicando un texto"

# Clase derivada Imagen
class Imagen(Publicacion):
    def mostrar(self):
        return "Publicando una imagen"

# Clase derivada Video
class Video(Publicacion):
    def mostrar(self):
        return "Publicando un video"

# Ejemplo de uso
publicacion_texto = Texto()
publicacion_imagen = Imagen()
publicacion_video = Video()

print(publicacion_texto.mostrar())  # Publicando un texto
print(publicacion_imagen.mostrar())  # Publicando una imagen
print(publicacion_video.mostrar())   # Publicando un video


8.
# Clase base MétodoPago
class MetodoPago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada TarjetaCredito
class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pagando {monto} usando Tarjeta de Crédito"

# Clase derivada PayPal
class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pagando {monto} usando PayPal"

# Clase derivada TransferenciaBancaria
class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pagando {monto} usando Transferencia Bancaria"

# Ejemplo de uso
pago_tarjeta = TarjetaCredito()
pago_paypal = PayPal()
pago_transferencia = TransferenciaBancaria()

print(pago_tarjeta.procesar_pago(100))  # Pagando 100 usando Tarjeta de Crédito
print(pago_paypal.procesar_pago(150))   # Pagando 150 usando PayPal
print(pago_transferencia.procesar_pago(200))  # Pagando 200 usando Transferencia Bancaria
