# Clase base Instrumento
class Instrumento:
    def tocar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase derivada Guitarra
class Guitarra(Instrumento):
    def tocar(self):
        return "La guitarra está sonando: strum strum."

# Clase derivada Piano
class Piano(Instrumento):
    def tocar(self):
        return "El piano está sonando: plink plonk."

# Clase derivada Batería
class Bateria(Instrumento):
    def tocar(self):
        return "La batería está sonando: boom boom."

#  uso
guitarra = Guitarra()
piano = Piano()
bateria = Bateria()

print(guitarra.tocar())
print(piano.tocar())
print(bateria.tocar())


# Crear una clase base llamada Instrumento con un método tocar. Luego,
# crea 3 clases derivadas como Guitarra, Piano y Bateria, donde cada una implemente el método
# tocar y retorne su propio sonido.