# main.py
from producto import Producto
from inventario2 import Inventario

def menu():
    print("\n----- MENÚ DE INVENTARIO -----")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto por nombre")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == "1":
            inventario.mostrar_inventario()

        elif opcion == "2":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: cantidad y precio deben ser números.")
                continue
            p = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(p)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
            except ValueError:
                print("Error: cantidad y precio deben ser números.")
                continue
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
