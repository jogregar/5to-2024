""" class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"

class Gallina(Animal):
    def hacer_sonido(self):
        return "Cloc cloc"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

animales = [Vaca(), Gallina(), Perro()]

for animal in animales:
    print(f"El {animal.__class__.__name__} hace: {animal.hacer_sonido()}") """




class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripción(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Coche(Vehículo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas

    def descripción(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de puertas: {self.num_puertas}"

class Motocicleta(Vehículo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripción(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindrada: {self.cilindrada} cc"

class Camión(Vehículo):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def descripción(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Capacidad de carga: {self.capacidad_carga} kg"

# Ejemplo de uso
vehículos = [
    Coche("Toyota", "Corolla", 4),
    Motocicleta("Yamaha", "MT-07", 689),
    Camión("Volvo", "FH16", 25000)
]

for vehículo in vehículos:
    print(vehículo.descripción())