class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas
    
    def __str__(self):
        return f"la marca del auto es {self.marca}, el modelo es {self.modelo} y tiene {self.numero_de_puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f"la marca de la moticicleta es {self.marca}, el modelo es {self.modelo} y tiene {self.cilindrada} de cilindrada"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, capacidad_de_carga):
        super().__init__(marca, modelo)
        self.capacidad_de_carga = capacidad_de_carga
        
    def __str__(self):
        return f"la marca del camion es {self.marca}, el modelo es {self.modelo} y tiene una capacidad de carga de {self.capacidad_de_carga} Kg"

coche = Coche("Toyota", "Corolla", 4)
moto = Motocicleta("Yamaha", "MT-07", 689)
camion = Camion("Volvo", "FH16", 25000)

print(coche)
print(moto)
print(camion)
