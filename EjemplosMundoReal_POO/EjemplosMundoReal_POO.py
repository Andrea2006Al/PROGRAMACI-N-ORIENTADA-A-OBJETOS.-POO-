# Clase que representa una mascota
class Mascota:
    def __init__(self, nombre, especie, edad, dueño):
        self.nombre = nombre         # Nombre de la mascota
        self.especie = especie       # Tipo de animal (gato, perro, etc.)
        self.edad = edad             # Edad en años
        self.dueño = dueño           # Nombre del dueño

    def mostrar_info(self):
        print(f"{self.nombre} ({self.especie}, {self.edad} años) - Dueño: {self.dueño}")


# Clase que representa la veterinaria
class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []  # Lista para guardar las mascotas registradas

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Se ha registrado a {mascota.nombre} en la veterinaria {self.nombre}.")

    def mostrar_mascotas(self):
        print(f"\nMascotas registradas en {self.nombre}:")
        if not self.mascotas:
            print("Aún no hay mascotas registradas.")
        else:
            for m in self.mascotas:
                m.mostrar_info()


# prueba del sistema.

# Crear una veterinaria
mi_veterinaria = Veterinaria("Veterinaria San Martín")

# Crear algunas mascotas
mascota1 = Mascota("Rocky", "Perro", 3, "Andrea Gavilanes")
mascota2 = Mascota("Safiro", "Gato", 2, "Juan Peña")

# Registrar las mascotas en la veterinaria
mi_veterinaria.registrar_mascota(mascota1)
mi_veterinaria.registrar_mascota(mascota2)

# Mostrar mascotas registradas
mi_veterinaria.mostrar_mascotas()
