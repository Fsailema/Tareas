
class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} ({self.duracion} mins) - {self.genero}"

class Sala:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad

    def mostrar_info(self):
        return f"Sala {self.numero} - Capacidad: {self.capacidad} asientos"

    def ocupar_asientos(self, cantidad):
        if cantidad <= self.asientos_disponibles:
            self.asientos_disponibles -= cantidad
            print(f"Se han ocupado {cantidad} asientos en la sala {self.numero}")
        else:
            print("No hay suficientes asientos disponibles en esta sala")

class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)
        print(f"Se ha agregado la sala {sala.numero} al cine")

    def mostrar_salas(self):
        if not self.salas:
            print("No hay salas disponibles en este cine")
        else:
            print("Salas disponibles en el cine:")
            for sala in self.salas:
                print(sala.mostrar_info())

# Creación de películas
pelicula1 = Pelicula("Inception", 148, "Ciencia Ficción")
pelicula2 = Pelicula("The Godfather", 175, "Drama")

# Creación de salas
sala1 = Sala(1, 50)
sala2 = Sala(2, 40)

# Creación del cine
cine = Cine("Cineplex")

# Agregar salas al cine
cine.agregar_sala(sala1)
cine.agregar_sala(sala2)

# Mostrar salas disponibles
cine.mostrar_salas()

# Ocupar asientos en una sala
sala_seleccionada = cine.salas[0]
sala_seleccionada.ocupar_asientos(45)

# Mostrar información actualizada de las salas
cine.mostrar_salas()
