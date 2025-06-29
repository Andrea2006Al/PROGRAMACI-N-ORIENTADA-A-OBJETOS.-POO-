# Programa: Cálculo del área de un rectángulo
# Este programa solicita al usuario la base y altura de un rectángulo,
# calcula su área y muestra si el área es mayor a un valor específico.

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo dado su base y altura."""
    area = base * altura
    return area

# Solicitar datos al usuario
nombre_usuario = input("¿Cual es tu nombre?: ")
base_rectangulo = float(input("Insertar la base del rectángulo (cm): "))
altura_rectangulo = float(input("Insertar la altura del rectángulo (cm): "))
umbral_area = 500.00  # Valor de comparación

# Cálculo del área
area_total = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Verificación booleana
es_mayor_a_umbral = area_total > umbral_area

# Mostrar resultados
print(f"\nHola, {nombre_usuario}.")
print(f"El área del rectángulo es: {area_total} cm².")
print(f"¿El área es mayor a {umbral_area} cm²? {es_mayor_a_umbral}")
