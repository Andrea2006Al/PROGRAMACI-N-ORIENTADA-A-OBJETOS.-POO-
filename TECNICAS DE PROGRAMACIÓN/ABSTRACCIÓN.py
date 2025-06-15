# Clase vehiculo
class Vehiculo:
    # Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Crear objetos vehiculo
vehiculo1 = Vehiculo("Chevrolet", "Sedan")
vehiculo2 = Vehiculo("Mazda", "Convertible")

# Imprimir la marca de los vehículos
print(vehiculo1.marca)
print(vehiculo2.marca)

