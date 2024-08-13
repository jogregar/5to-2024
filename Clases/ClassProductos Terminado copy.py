import os

class Articulos:
    def __init__ (self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
        }
        if self.buscar_producto(nombre):
            return "Producto ya existe"
        else:
            self.productos.append(producto)
            return "Producto Agregado"

    def listar_producto(self):
        for producto in self.productos:
            print ("nombre: ", producto["nombre"], " precio: ", 
            producto["precio"], " Cantidad: ", producto["cantidad"])


    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                return producto
        return False
        
    def modificar_producto(self, nombre, precio, cantidad):
        producto = self.buscar_producto(nombre)
        if producto:
            producto["precio"] = precio
            producto["cantidad"] = cantidad
            return "Producto Modificado"
        return "Producto no Existe"

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return "Producto Eliminado"
        return "Producto no Existe"
    
productos = Articulos()

op = -1
while op != 0:
    os.system("cls")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Modificar Producto")
    print("4. Eliminar Producto")
    print("0. Salir")
    op = int(input("Ingrese Opcion: "))
    os.system("cls")
    match op:
        case 1:
            nombre = input("Nombre del Producto: ")
            precio = input("Precio del Producto: ")
            cantidad = input("Cantidad del Prpducto: ")
            print (productos.agregar_producto(nombre, precio, cantidad))
        case 2:
            productos.listar_producto()
        case 3:
            nombre = input("Nombre del Producto a buscar: ")
            precio = input("Nuevo Precio del Producto: ")
            cantidad = input("Nueva Cantidad del Prpducto: ")
            print (productos.modificar_producto(nombre, precio, cantidad))
        case 4:
            nombre = input("Nombre del Producto a eliminar: ")
            print(productos.eliminar_producto(nombre))

    input("Presione Enter para continuar")
