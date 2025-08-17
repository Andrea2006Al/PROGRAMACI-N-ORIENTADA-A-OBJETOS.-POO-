from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # Lista de objetos Producto

    def agregar_producto(self, producto):
        # Validar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe. No se puede agregar el producto.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
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
            print("Lista de productos en inventario:")
            for p in self.productos:
                print(p)
