# Programa tradicional para sacar el promedio de temperaturas en una semana

def pedir_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input("Temperatura del día " + str(i + 1) + ": "))
        temperaturas.append(temp)
    return temperaturas

def sacar_promedio(lista):
    return sum(lista) / len(lista)

# Programa principal
temps = pedir_temperaturas()
promedio = sacar_promedio(temps)
print("El promedio semanal es:", round(promedio, 2), "°C")


