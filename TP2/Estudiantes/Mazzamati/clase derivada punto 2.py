class Instrumento:
    def tocar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Guitarra(Instrumento):
    def tocar(self):
        return "La guitarra está sonando: ran ran"

class Piano(Instrumento):
    def tocar(self):
        return "El piano está sonando: pin pin"

class Bateria(Instrumento):
    def tocar(self):
        return "La batería está sonando: boom boom"

# Ejemplo de uso
guitarra = Guitarra()
piano = Piano()
bateria = Bateria()

print(guitarra.tocar())
print(piano.tocar())
print(bateria.tocar())
