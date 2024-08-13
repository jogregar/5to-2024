import os

class Biblioteca:
    def __init__ (self):
        self.libros = []

    def agregar_libro(self, titulo, autor, anio):
        libro = {
            "titulo":titulo,
            "autor":autor,
            "anio":anio
        }
        if self.buscar_libro(titulo):
            return "Libro ya existe"
        else:
            self.libros.append(libro)
            return "Libro Agregado"

    def listar_libros(self):
        for libro in self.libros:
            print ("Titulo: ", libro["titulo"], " Autor: ", 
            libro["autor"], " Año: ", libro["anio"])


    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo:
                return libro
        return False
        
    def modificar_libro(self, titulo, autor, anio):
        libro = self.buscar_libro(titulo)
        if libro:
            libro["autor"] = autor
            libro["anio"] = anio
            return "Libro Modificado"
        return "Libro no Existe"

    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            self.libros.remove(libro)
            return "Libro Eliminado"
        return "Libro no Existe"
    
libros = Biblioteca()

op = -1
while op != 0:
    os.system("cls")
    print("1. Agregar Libro")
    print("2. Listar Libros")
    print("3. Modificar Libro")
    print("4. Eliminar Libro")
    print("0. Salir")
    op = int(input("Ingrese Opcion: "))
    os.system("cls")
    match op:
        case 1:
            articulo = input("Titulo del Libro: ")
            autor = input("Autor del Libro: ")
            anio = input("Año del Libro: ")
            print (libros.agregar_libro(articulo, autor, anio))
        case 2:
            libros.listar_libros()
        case 3:
            articulo = input("Titulo del Libro: ")
            autor = input("Autor del Libro: ")
            anio = input("Año del Libro: ")
            print (libros.modificar_libro(articulo, autor, anio))
        case 4:
            articulo = input("Titulo Del Libro a eliminar: ")
            print(libros.eliminar_libro(articulo))

    input("Presione Enter para continuar")
