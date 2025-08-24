# inventario.py
from producto import Producto

class Inventario:
    def __init__(self, archivo="prueba1.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    # Guardar todos los productos en archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(p.to_line())
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    # Cargar productos desde archivo
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos.append(producto)
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe. No se puede agregar el producto.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado y guardado exitosamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado y archivo actualizado.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_en_archivo()
                print("Producto actualizado y archivo guardado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for p in self.productos:
                print(p)

