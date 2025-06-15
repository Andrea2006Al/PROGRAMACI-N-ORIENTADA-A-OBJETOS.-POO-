# Programa usando clases para sacar el promedio de temperaturas

class Clima:
    def __init__(self):
        self.temperaturas = []

    def agregar(self, temp):
        self.temperaturas.append(temp)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
semana = Clima()
for i in range(7):
    temp = float(input("Temperatura del día " + str(i + 1) + ": "))
    semana.agregar(temp)

print("El promedio semanal es:", round(semana.promedio(), 2), "°C")
