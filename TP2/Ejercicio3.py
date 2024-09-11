class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío!"


perro = Perro()
gato = Gato()
pajaro = Pajaro()

print (f"El perro hace {perro.hacer_sonido()}")
print (f"El gato hace {gato.hacer_sonido()}")
print (f"El pajaro hace {pajaro.hacer_sonido()}")
