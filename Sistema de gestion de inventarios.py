
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar si el ID es único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        if resultados:
            print("Resultados de búsqueda:")
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            print("Inventario:")
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("El inventario está vacío.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear inventario
    inventario = Inventario()

    # Agregar productos
    producto1 = Producto(1, "Camiseta", 10, 15.99)
    producto2 = Producto(2, "Pantalón", 5, 29.99)
    producto3 = Producto(3, "Medias", 20, 4.99)

    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Buscar producto por nombre
    inventario.buscar_producto_por_nombre("pantalón")

    # Actualizar cantidad y precio de un producto
    inventario.actualizar_producto(2, cantidad=7, precio=34.99)

    # Mostrar inventario actualizado
    inventario.mostrar_inventario()

    # Eliminar un producto
    inventario.eliminar_producto(3)

    # Mostrar inventario después de eliminar un producto
    inventario.mostrar_inventario()