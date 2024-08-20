class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau..!"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau.!"

class Pato(Animal):
    def hacer_sonido(self):
        return "Cua.!"
    
mi_perro = Perro()
mi_gato = Gato()
mi_pato = Pato()

print (mi_perro.hacer_sonido())
print (mi_gato.hacer_sonido())
print (mi_pato.hacer_sonido())

    
