class Ave:
    def hablar(self):
        print("Pío pío")

class Perro:
    def hablar(self):
        print("Guau guau")

class Gato:
    def hablar(self):
        print("Miau")

# Función que demuestra polimorfismo
def hacer_hablar(animal):
    animal.hablar()

# Lista de distintos animales
animales = [Ave(), Perro(), Gato()]

# Todos los objetos responden al mismo método aunque sean de clases diferentes
if __name__ == "__main__":
    for a in animales:
        hacer_hablar(a)
