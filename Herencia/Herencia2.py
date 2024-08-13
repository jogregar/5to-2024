class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def descripcion(self):
        return (f"Este es un {self.marca} {self.modelo}")
    
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        # self.marca = marca
        # self.modelo = modelo
        self.puertas = puertas

    def descripcion(self):
        return (f"Este es un {self.marca} {self.modelo} y tiene {self.puertas} puertas")

mi_auto = Auto("chevrolet", "Onix", 4)
print(mi_auto.descripcion())