# Sistema Avanzado de Gestión de Inventario
# -----------------------------------------
# Modulos:
# - Clase Producto
# - Clase Inventario
# - Menú interactivo de consola
# - Guardado y carga en archivo JSON

import json
from pathlib import Path

# -------------------------
# Clase Producto
# -------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"Producto(ID={self.id}, Nombre={self.nombre}, Cantidad={self.cantidad}, Precio={self.precio})"

    def actualizar_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.cantidad = cantidad

    def ajustar_cantidad(self, delta):
        if self.cantidad + delta < 0:
            raise ValueError("No hay suficiente stock")
        self.cantidad += delta

    def actualizar_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self.precio = precio

    def a_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def desde_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


# -------------------------
# Clase Inventario
# -------------------------
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: clave=ID, valor=Producto

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            raise ValueError("Ya existe un producto con ese ID")
        self.productos[producto.id] = producto

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        del self.productos[id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        prod = self.productos[id_producto]
        if cantidad is not None:
            prod.actualizar_cantidad(cantidad)
        if precio is not None:
            prod.actualizar_precio(precio)

    def ajustar_cantidad_producto(self, id_producto, delta):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        self.productos[id_producto].ajustar_cantidad(delta)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        return list(self.productos.values())

    def guardar_archivo(self, ruta="inventario.json"):
        data = [p.a_dict() for p in self.productos.values()]
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def cargar_archivo(self, ruta="inventario.json"):
        if not Path(ruta).exists():
            return
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.productos.clear()
            for d in data:
                p = Producto.desde_dict(d)
                self.productos[p.id] = p


# -------------------------
# Menú interactivo
# -------------------------
def menu():
    inv = Inventario()
    inv.cargar_archivo()

    while True:
        print("\n=== Menú Inventario ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Ajustar cantidad (+/-)")
        print("5. Actualizar precio")
        print("6. Buscar por nombre")
        print("7. Mostrar todos")
        print("8. Guardar inventario")
        print("0. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            try:
                idp = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inv.agregar_producto(Producto(idp, nombre, cantidad, precio))
                print("Producto agregado.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "2":
            try:
                idp = input("ID del producto a eliminar: ")
                inv.eliminar_producto(idp)
                print("Producto eliminado.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "3":
            try:
                idp = input("ID del producto a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                inv.actualizar_producto(idp, cantidad=cantidad)
                print("Cantidad actualizada.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "4":
            try:
                idp = input("ID del producto: ")
                delta = int(input("Ajuste (+/-): "))
                inv.ajustar_cantidad_producto(idp, delta)
                print("Cantidad ajustada.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "5":
            try:
                idp = input("ID del producto: ")
                precio = float(input("Nuevo precio: "))
                inv.actualizar_producto(idp, precio=precio)
                print("Precio actualizado.")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "6":
            nombre = input("Buscar por nombre: ")
            resultados = inv.buscar_por_nombre(nombre)
            for p in resultados:
                print(p)

        elif opcion == "7":
            for p in inv.mostrar_todos():
                print(p)

        elif opcion == "8":
            inv.guardar_archivo()
            print("Inventario guardado.")

        elif opcion == "0":
            inv.guardar_archivo()
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
