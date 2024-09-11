class Publicacion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        pass

class Libro(Publicacion):
    def __init__(self, titulo, autor, num_paginas):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas
    
    def mostrar_info(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}"

class Revista(Publicacion):
    def __init__(self, titulo, autor, numero):
        super().__init__(titulo, autor)
        self.numero = numero
    
    def mostrar_info(self):
        return f"Revista: {self.titulo}, Autor: {self.autor}, Número: {self.numero}"

class Periodico(Publicacion):
    def __init__(self, titulo, autor, fecha):
        super().__init__(titulo, autor)
        self.fecha = fecha
    
    def mostrar_info(self):
        return f"Periódico: {self.titulo}, Autor: {self.autor}, Fecha: {self.fecha}"

# Función para mostrar la información de todas las publicaciones
def mostrar_publicaciones(publicaciones):
    for publicacion in publicaciones:
        print(publicacion.mostrar_info())

# Ejemplo de uso
publicaciones = [
    Libro("El Principito", "Antoine de Saint-Exupéry", 96),
    Revista("National Geographic", "Varios Autores", 101),
    Periodico("El País", "Varios Autores", "2024-08-19")
]

mostrar_publicaciones(publicaciones)