class Publicacion:
    def mostrar(self):
        pass

class Texto(Publicacion):
    def __init__(self, contenido):
        self.contenido = contenido

    def mostrar(self):
        return f"El Texto publicado es: {self.contenido}"

class Imagen(Publicacion):
    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar(self):
        return f"la imagen publicada es: {self.archivo}"

class Video(Publicacion):
    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar(self):
        return f"El video publicado es: {self.archivo}"

texto = Texto("Hola a todos!")
imagen = Imagen("foto.jpg")
video = Video("video.mp4")


print (texto.mostrar())
print (imagen.mostrar())
print (video.mostrar())