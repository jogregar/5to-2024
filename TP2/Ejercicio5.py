class Dispositivo:
    def encender(self):
        pass

class Television(Dispositivo):
    def encender(self):
        return "Encendiendo la televisión..."

class Radio(Dispositivo):
    def encender(self):
        return "Encendiendo la radio..."

class Computadora(Dispositivo):
    def encender(self):
        return "Encendiendo la computadora..."


television = Television()
radio = Radio()
computadora = Computadora()

print (television.encender())
print (radio.encender())
print (computadora.encender())