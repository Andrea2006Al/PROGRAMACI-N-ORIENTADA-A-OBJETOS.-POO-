# -------------------------------
# Clase Libro
# -------------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Título y autor como tupla (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# -------------------------------
# Clase Usuario
# -------------------------------
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


# -------------------------------
# Clase Biblioteca
# -------------------------------
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario {user_id: Usuario}
        self.ids_registrados = set()  # Conjunto para asegurar IDs únicos

    # --------- Gestión de libros ---------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No se encontró el libro con ese ISBN.")

    # --------- Gestión de usuarios ---------
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.ids_registrados:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.user_id] = usuario
            self.ids_registrados.add(usuario.user_id)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios.pop(user_id)
            self.ids_registrados.remove(user_id)
            print(f"Usuario dado de baja: {usuario}")
        else:
            print("No se encontró al usuario con ese ID.")

    # --------- Préstamos ---------
    def prestar_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro} → {usuario.nombre}")

    def devolver_libro(self, user_id, isbn):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                print(f"Libro devuelto: {libro} por {usuario.nombre}")
                return
        print("Ese usuario no tiene el libro prestado.")

    # --------- Búsqueda de libros ---------
    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if "titulo" in kwargs and kwargs["titulo"].lower() in libro.info[0].lower():
                resultados.append(libro)
            elif "autor" in kwargs and kwargs["autor"].lower() in libro.info[1].lower():
                resultados.append(libro)
            elif "categoria" in kwargs and kwargs["categoria"].lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # --------- Listar libros prestados ---------
    def listar_libros_prestados(self, user_id):
        if user_id not in self.usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[user_id]
        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")


# -------------------------------
# Menú interactivo
# -------------------------------
def menu():
    biblioteca = Biblioteca()

    # libros de ejemplo
    biblioteca.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111"))
    biblioteca.agregar_libro(Libro("El Quijote", "Miguel de Cervantes", "Clásico", "222"))
    biblioteca.agregar_libro(Libro("Python para Todos", "Raúl González", "Programación", "333"))
    biblioteca.agregar_libro(Libro("La Odisea", "Homero", "Épico", "444"))

    while True:
        print("\n===== Menú Biblioteca Digital =====")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados de un usuario")
        print("9. Mostrar catálogo disponible")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "2":
            isbn = input("Ingrese ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))

        elif opcion == "4":
            user_id = input("Ingrese ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input("Ingrese valor de búsqueda: ")
            if criterio in ["titulo", "autor", "categoria"]:
                resultados = biblioteca.buscar_libro(**{criterio: valor})
                if resultados:
                    print("Resultados encontrados:")
                    for libro in resultados:
                        print(f"  - {libro}")
                else:
                    print("No se encontraron resultados.")
            else:
                print("Criterio inválido.")

        elif opcion == "8":
            user_id = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(user_id)

        elif opcion == "9":
            if biblioteca.libros:
                print("Catálogo de libros disponibles:")
                for libro in biblioteca.libros.values():
                    print(f"  - {libro}")
            else:
                print("No hay libros disponibles en la biblioteca.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()

