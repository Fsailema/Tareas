
# Este programa calcula el área de un triángulo dados la base y la altura.

def calcular_area_triangulo(base, altura):
    # Fórmula para calcular el área del triángulo: (base * altura) / 2
    area = round((base * altura) / 2,2)
    return area

# Solicitar al usuario la base y la altura del triángulo

base_triangulo = float(input("Ingresa la longitud de la base del triángulo: "))
altura_triangulo = float(input("Ingresa la altura del triángulo: "))

# Calcular el área del triángulo utilizando la función
area_del_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Mostrar el resultado al usuario
print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_del_triangulo}")