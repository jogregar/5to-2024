# Clase base Dispositivo
class Dispositivo:
    def encender(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada Televisión
class Television(Dispositivo):
    def encender(self):
        return "La televisión se está encendiendo."

# Clase derivada Radio
class Radio(Dispositivo):
    def encender(self):
        return "La radio se está encendiendo."

# Clase derivada Computadora
class Computadora(Dispositivo):
    def encender(self):
        return "La computadora se está encendiendo."

 
tv = Television()
radio = Radio()
computadora = Computadora()

print(tv.encender())
print(radio.encender())
print(computadora.encender())


# . Crear una clase base llamada Dispositivo con un método encender.
# Luego, crea 3 clases derivadas Televisión, Radio y Computadora, 
# donde cada una implemente el método encender y retorne que el dispositivo se está encendiendo.