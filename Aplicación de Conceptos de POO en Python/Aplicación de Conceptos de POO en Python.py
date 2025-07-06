# Clase base: Mascota
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Encapsulación

    def hacer_sonido(self):
        return "Hace un sonido..."

    def mostrar_info(self):
        return f"{self.nombre}, {self.__edad} años"

    def get_edad(self):  # Getter (encapsulación)
        return self.__edad

    def set_edad(self, nueva_edad):  # Setter
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")


# Clase derivada: Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):  # Polimorfismo
        return "Guau guau"

    def mostrar_info(self):
        return f"Perro: {self.nombre}, Raza: {self.raza}, Edad: {self.get_edad()}"


# Clase derivada: Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):  # Polimorfismo
        return "Miau"

    def mostrar_info(self):
        return f"Gato: {self.nombre}, Color: {self.color}, Edad: {self.get_edad()}"


# Polimorfismo con función externa
def mostrar_sonido(mascota):
    print(f"{mascota.nombre} dice: {mascota.hacer_sonido()}")


# ----------- PROGRAMA PRINCIPAL -----------

# Crear objetos
perro1 = Perro("Rocky", 4, "Labrador")
gato1 = Gato("Simba", 2, "Negro")

# Mostrar información
print(perro1.mostrar_info())
print(gato1.mostrar_info())

# Probar sonidos
mostrar_sonido(perro1)
mostrar_sonido(gato1)

# Usar encapsulación
print(f"Edad de {perro1.nombre}: {perro1.get_edad()} años")
perro1.set_edad(5)
print(f"Edad actualizada de {perro1.nombre}: {perro1.get_edad()} años")
