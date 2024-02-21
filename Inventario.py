
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self, archivo):
        self.productos = []
        self.archivo = archivo

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    codigo, nombre, precio = line.strip().split(',')
                    self.productos.append(Producto(codigo, nombre, float(precio)))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("Permiso denegado para acceder al archivo de inventario.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.codigo},{producto.nombre},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Permiso denegado para guardar el archivo de inventario.")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()

    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.nombre = nuevo_nombre
                producto.precio = nuevo_precio
                self.guardar_inventario()
                return True
        return False

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                self.guardar_inventario()
                return True
        return False


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario("inventario.txt")
    inventario.cargar_inventario()

    # Operaciones de prueba
    producto_nuevo = Producto("001", "Producto1", 10.99)
    inventario.agregar_producto(producto_nuevo)

    inventario.actualizar_producto("001", "Nuevo Producto", 15.99)

    inventario.eliminar_producto("001")

