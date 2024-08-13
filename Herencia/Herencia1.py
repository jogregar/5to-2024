class Animal:
    def __init__ (self, nombre):
        self.nombre = nombre

    def hablar(self):
#        print(self.nombre, "Hace un sonido")
        return (self.nombre + " Hace un sonido")

class Perro(Animal):
    def hablar(self):
        #print (self.nombre, "Ladra")
        #return (self.nombre + " Ladra")
        return (f"{self.nombre} Ladra")

class Gato(Animal):
    def hablar(self):
        #print(self.nombre, "Miau")
        #return (self.nombre + " Miau")
        return (f"{self.nombre} Maiu")

mi_perro = Perro("Rex")
print(mi_perro.hablar())

mi_gato = Gato("Firulay")
print(mi_gato.hablar())
