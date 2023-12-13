
# Función para ingresar datos diarios de temperatura

def ingresar_temperaturas_diarias():
    temperaturas = []  # Lista para almacenar las temperaturas diarias
    for i in range(7):  # Se ingresan datos para una semana (7 días)
        temperatura = float(input(f"Ingrese la temperatura para el día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas


# Función para calcular el promedio semanal de temperaturas

def calcular_promedio_semanal(temperaturas_semana):
    suma_temperaturas = sum(temperaturas_semana)
    promedio_semanal = suma_temperaturas / len(temperaturas_semana)
    return promedio_semanal


# Función principal que llama a las otras funciones y muestra el resultado

def main():
    print("Ingrese las temperaturas diarias de la semana:")
    temperaturas_semana = ingresar_temperaturas_diarias()  # Ingreso de temperaturas
    promedio = calcular_promedio_semanal(temperaturas_semana)  # Cálculo del promedio

    print("\nLas temperaturas ingresadas son:", temperaturas_semana)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")


# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()