class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "Strum de guitarra"

class Piano(Instrumento):
    def tocar(self):
        return "Plink plonk del piano"

class Bateria(Instrumento):
    def tocar(self):
        return "Bum bum tss de la batería"

guitarra = Guitarra()
piano = Piano()
bateria = Bateria()


print (guitarra.tocar())
print (piano.tocar())
print (bateria.tocar())