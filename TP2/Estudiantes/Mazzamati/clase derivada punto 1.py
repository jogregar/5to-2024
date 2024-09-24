class Dispositivo:
    def encender(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Television(Dispositivo):
    def encender(self):
        return "La televisión se está encendiendo"

class Radio(Dispositivo):
    def encender(self):
        return "La radio se está encendiendo"

class Computadora(Dispositivo):
    def encender(self):
        return "La computadora se está encendiendo"

# Ejemplo de uso
television = Television()
radio = Radio()
computadora = Computadora()

print(television.encender())
print(radio.encender())
print(computadora.encender())
