class Libros:

    def __init__(self, titulo, autor, annio, edicion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.annio = annio
        self.edicion = edicion
        self.paginas = paginas

    def mostrar_informacion(self):
        print(self.titulo, self.autor, self.annio, self.edicion, self.paginas)

    
    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

libro1 = Libros("Python", "Pedro", 2000, "1ra", 300)

libro1.mostrar_informacion()

libro1.cambiar_titulo("Python Avanzado")

libro1.mostrar_informacion()


