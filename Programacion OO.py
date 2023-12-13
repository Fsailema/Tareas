
class InformacionClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas diarias

    def ingresar_temperatura(self):
        temperatura = float(input("Ingrese la temperatura para hoy: "))
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) != 7:
            print("Por favor ingrese las temperaturas de los 7 días de la semana.")
            return None
        suma_temperaturas = sum(self.temperaturas)
        promedio_semanal = suma_temperaturas / len(self.temperaturas)
        return promedio_semanal


def main():
    info_clima = InformacionClimaDiario()

    print("Ingrese las temperaturas diarias de la semana:")
    for dia in range(7):
        print(f"Día {dia + 1}:")
        info_clima.ingresar_temperatura()

    promedio = info_clima.calcular_promedio_semanal()

    if promedio is not None:
        print("\nLas temperaturas ingresadas son:", info_clima.temperaturas)
        print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")


if __name__ == "__main__":
    main()