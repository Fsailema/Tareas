
class InformacionClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura para el día {dia + 1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) != 7:
            print("Por favor ingrese las temperaturas de los 7 días de la semana.")
            return None
        suma_temperaturas = sum(self.temperaturas)
        promedio_semanal = suma_temperaturas / len(self.temperaturas)
        return promedio_semanal


info_clima = InformacionClimaDiario()
info_clima.ingresar_temperaturas()

promedio = info_clima.calcular_promedio_semanal()

if promedio is not None:
    print("\nLas temperaturas ingresadas son:", info_clima.temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")