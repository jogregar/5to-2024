class Volador:
    def volar(self):
        return ("Estoy volando")
    
class Nadador:
    def nadar(self):
        return ("Estoy nadando")
    
class Pato(Volador, Nadador):
    def hacer_sonido(self):
        return ("Cua, Cua")

mi_pato = Pato()
print (mi_pato.volar())
print (mi_pato.nadar())
print (mi_pato.hacer_sonido())
