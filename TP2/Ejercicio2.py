class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

cuadrado = Cuadrado(4)
triangulo = Triangulo(3, 6)
circulo = Circulo(5)
print(f"El área del cuadrado es: {cuadrado.area()}") 
print(f"El área del triangulo es: {triangulo.area():.2f}") 
print(f"El área del circulo es: {circulo.area():.2f}") 