class Autos:
    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
    
    def poner_marcha(self):
        print("El auto esta en marcha")

    def acelerar(self):
        print("El auto esta acelerando")

    def frenar(self):
        print("el auto esta frenando")

    def retroceder(self):
        print("el auto esta retrocediendo")

auto1 = Autos("Chevrolet", "Onix", "Negro", 260)
auto2 = Autos("Fiat", "Cronos", "Verde", 230)
auto1.poner_marcha()
auto1.acelerar()
auto1.frenar()
auto1.retroceder()