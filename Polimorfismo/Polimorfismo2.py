class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def area(self, radio):
        return 3.1415 * radio ** 2
    
class Rectangulo(Forma):
    def area(self, base, altura):
        return base * altura
    
class Triangulo(Forma):
    def area(self, base, altura):
        return (base * altura) / 2
    
area_circulo = Circulo()
area_rectangulo = Rectangulo()
area_triangulo = Triangulo()

print (f"El área del circulo es: {area_circulo.area(10):.2f}")
print (f"el área del rectangulo es: {area_rectangulo.area(10,20)}")
print (f"El área del triangulo es: {area_triangulo.area(10,10)}")