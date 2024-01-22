
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Se ha creado la cuenta de {self.titular} con un saldo inicial de {self.saldo}.")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} en la cuenta de {self.titular}. Saldo actual: {self.saldo}.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta de {self.titular}. Saldo actual: {self.saldo}.")
        else:
            print("Saldo insuficiente. No se puede realizar la operación.")

    def __del__(self):
        print(f"Se está cerrando la cuenta de {self.titular}. Saldo final: {self.saldo}.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta bancaria
    cuenta_favio = CuentaBancaria("Favio", saldo_inicial=100)

    # Realizar transacciones
    cuenta_favio.depositar(100)
    cuenta_favio.retirar(300)

    # Eliminar la cuenta (se llama automáticamente al destructor __del__)
    del cuenta_favio