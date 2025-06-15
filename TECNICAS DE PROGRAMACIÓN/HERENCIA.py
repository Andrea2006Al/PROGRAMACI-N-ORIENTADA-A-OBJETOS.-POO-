# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} hace un sonido.")

# Clase derivada 1
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Guau")

# Clase derivada 2
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Miau")

# Programa principal de prueba
if __name__ == "__main__":
    animales = [Perro("Firulais"), Gato("Mishi")]
    for animal in animales:
        animal.hablar()
