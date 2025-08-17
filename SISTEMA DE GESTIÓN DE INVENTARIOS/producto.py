# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad en inventario
        :param precio: Precio unitario
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Representación del producto
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"
