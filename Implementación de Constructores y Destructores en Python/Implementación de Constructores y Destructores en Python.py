class RegistroNotas:
    def __init__(self, estudiante):
        """
        Constructor: se ejecuta al crear el objeto.
        Inicializa el nombre del estudiante y una lista vacía de notas.
        """
        self.estudiante = estudiante
        self.notas = []
        print(f"Registro creado para el estudiante: {self.estudiante}")

    def agregar_nota(self, nota):
        """
        Agrega una nota al registro del estudiante.
        """
        self.notas.append(nota)
        print(f"Nota {nota} agregada para {self.estudiante}.")

    def promedio(self):
        """
        Calcula y devuelve el promedio de notas.
        """
        if self.notas:
            promedio = sum(self.notas) / len(self.notas)
            print(f"El promedio de {self.estudiante} es {promedio:.2f}")
        else:
            print(f"No hay notas registradas para {self.estudiante}.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto es eliminado.
        """
        print(f"Registro de {self.estudiante} ha sido cerrado.")
# Creamos un registro de notas para un estudiante
registro1 = RegistroNotas("Carlos Monar")

# Agregamos algunas notas
registro1.agregar_nota(10)
registro1.agregar_nota(9.0)
registro1.agregar_nota(4.5)

# Mostramos el promedio
registro1.promedio()

# Eliminamos el registro (activando el destructor)
del registro1
