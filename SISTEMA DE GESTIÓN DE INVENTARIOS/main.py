from Inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    menu()
