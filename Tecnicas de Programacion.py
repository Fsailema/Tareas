
#Abstraccion
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Uso de la abstracción
auto = Vehiculo("Toyota", "Corolla")

print(auto.obtener_info())

#Encapsulacion

class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado

    def depositar(self, monto):
        # Lógica para depositar fondos
        self.__saldo += monto

    def obtener_saldo(self):
        # Método para obtener el saldo
        return self.__saldo

# Uso de encapsulación
cuenta = CuentaBancaria()
cuenta.depositar(1000)
print(cuenta.obtener_saldo())

#Herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Método a ser implementado por las clases derivadas

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Uso de herencia
mi_perro = Perro("Bobby")
mi_gato = Gato("Pelusa")

print(mi_perro.hacer_sonido())
print(mi_gato.hacer_sonido())


#Polimorfismo

class Figura:
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio

# Uso de polimorfismo
mi_cuadrado = Cuadrado(5)
mi_circulo = Circulo(3)

print(mi_cuadrado.calcular_area())
print(mi_circulo.calcular_area())