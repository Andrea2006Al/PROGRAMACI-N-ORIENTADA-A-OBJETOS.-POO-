import os

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo .py dado su path.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)  # CAMBIO 1: ruta absoluta para seguridad
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Muestra el menú de scripts disponibles y permite seleccionar uno para visualizar su código.
    """
    ruta_base = os.path.dirname(__file__)  # Ruta donde se encuentra este archivo

    # CAMBIO 2: Menú expandido con rutas personalizadas por temas
    opciones = {
        '1': 'Aplicación de Conceptos de POO en Python/Aplicación de Conceptos de POO en Python.py',
        '2': 'Comparación de Programación Tradicional y POO en Python/Programación orientada a Objetos (POO).py',
        '2.1': 'Comparación de Programación Tradicional y POO en Python/Programación tradicional.py',
        '3': 'EjemplosMundoReal_POO/EjemplosMundoReal_POO.py',
        '4': 'Implementación de Constructores y Destructores en Python/Implementación de Constructores y Destructores en Python.py',
        '5': 'TECNICAS DE PROGRAMACIÓN/ABSTRACCIÓN.py',
        '5.1': 'TECNICAS DE PROGRAMACIÓN/ENCAPSULACION.py',
        '5.2': 'TECNICAS DE PROGRAMACIÓN/HERENCIA.py',
        '5.3': 'TECNICAS DE PROGRAMACIÓN/POLIMORFISMO.py',
        '6': 'TIPOS DE DATOS E IDENTIFICADORES/Tipos de datos e identificadores.py',
    }

    while True:
        # CAMBIO 3: Título decorativo del menú
        print("\n=========== DASHBOARD DE PROYECTOS - POO ===========\n")

        # CAMBIO 4: Ordenar las claves tipo '1', '2.1', etc.
        for key in sorted(opciones, key=lambda x: [int(p) if p.isdigit() else p for p in x.split('.')]):
            print(f"{key} - {opciones[key]}")
        print("\n0 - Salir")

        eleccion = input("\nElige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del Dashboard. ¡Hasta luego!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    mostrar_menu()
