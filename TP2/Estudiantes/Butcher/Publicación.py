
class Publicacion:
    def mostrar(self):
        raise NotImplementedError("Debes implementar el método mostrar en la clase derivada")

class Texto(Publicacion):
    def mostrar(self):
        return "Estoy publicando un texto"

class Imagen(Publicacion):
    def mostrar(self):
        return "Estoy publicando una imagen"

class Video(Publicacion):
    def mostrar(self):
        return "Estoy publicando un video"

texto = Texto()
imagen = Imagen()
video = Video()

print(texto.mostrar())  
print(imagen.mostrar())  
print(video.mostrar()) 