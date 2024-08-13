class Peliculas:
    
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

    def __str__(self):
        return (f"La pelicula {self.titulo}, su director es {self.director}, fue realizada en el año {self.anio}")
    
peliculas = Peliculas("Matrix", "José García", 2000)
print(peliculas)