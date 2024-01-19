
class Animal:
    def __init__(self, nombre, edad):
        # Atributos privados usando el prefijo '__'
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def hacer_sonido(self):
        return "El perro esta ladrando"


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase base usando super()
        super().__init__(nombre, edad)
        self.__raza = raza

    # Sobrescribimos el método hacer_sonido para el polimorfismo
    def hacer_sonido(self):
        return "¡Guau, guau!"

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza


# Crear instancias de las clases
animal_puro = Animal("Buddy", 5)
perro = Perro("Buddy", 3, "Labrador")

# Acceder a los métodos y atributos
print(f"{animal_puro.get_nombre()} tiene {animal_puro.get_edad()} años.")
print(f"{perro.get_nombre()} es un perro de raza {perro.get_raza()}.")

# Polimorfismo: el método hacer_sonido se comporta de manera diferente en cada clase
print(animal_puro.hacer_sonido())
print(perro.hacer_sonido())
print("Buddy has silencio")
