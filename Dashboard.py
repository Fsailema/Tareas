
import os

class Proyecto:
    def __init__(self, nombre, descripcion, ruta_script):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ruta_script = ruta_script

class Dashboard:
    def __init__(self):
        self.proyectos = []

    def agregar_proyecto(self, nombre, descripcion, ruta_script):
        proyecto = Proyecto(nombre, descripcion, ruta_script)
        self.proyectos.append(proyecto)

    def mostrar_codigo(self, ruta_script):
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_script_absoluta, 'r') as archivo:
                print(f"\n--- Código de {ruta_script} ---\n")
                print(archivo.read())
        except FileNotFoundError:
            print("El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    def mostrar_proyectos(self):
        print("\nProyectos en el Dashboard:")
        for i, proyecto in enumerate(self.proyectos, 1):
            print(f"{i}. {proyecto.nombre}")

    def mostrar_menu(self):
        while True:
            print("\nMenu Principal - Dashboard")
            print("1 - Mostrar Proyectos")
            print("2 - Agregar Proyecto")
            print("3 - Ver Código de un Proyecto")
            print("0 - Salir")

            eleccion = input("Selecciona una opción: ")
            if eleccion == '0':
                break
            elif eleccion == '1':
                self.mostrar_proyectos()
            elif eleccion == '2':
                nombre = input("Nombre del proyecto: ")
                descripcion = input("Descripción del proyecto: ")
                ruta_script = input("Ruta del script asociado al proyecto: ")
                self.agregar_proyecto(nombre, descripcion, ruta_script)
            elif eleccion == '3':
                self.mostrar_proyectos()
                seleccion = input("Selecciona el número de proyecto para ver su código: ")
                try:
                    seleccion = int(seleccion)
                    proyecto_seleccionado = self.proyectos[seleccion - 1]
                    self.mostrar_codigo(proyecto_seleccionado.ruta_script)
                except (ValueError, IndexError):
                    print("Selección no válida. Por favor, intenta de nuevo.")
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.mostrar_menu()