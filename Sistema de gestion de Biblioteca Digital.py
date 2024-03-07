
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.user_id)

    def dar_de_baja_usuario(self, usuario):
        if usuario.user_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario.user_id)

    def prestar_libro(self, libro, usuario):
        if libro.isbn in self.libros_disponibles and usuario.user_id in self.usuarios_registrados:
            usuario.prestar_libro(libro)
            del self.libros_disponibles[libro.isbn]

    def devolver_libro(self, libro, usuario):
        usuario.devolver_libro(libro)
        self.libros_disponibles[libro.isbn] = libro

    def buscar_libros_por_titulo(self, titulo):
        return [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo_autor[0].lower()]

    def buscar_libros_por_autor(self, autor):
        return [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.titulo_autor[1].lower()]

    def buscar_libros_por_categoria(self, categoria):
        return [libro for libro in self.libros_disponibles.values() if categoria.lower() == libro.categoria.lower()]

    def listar_libros_prestados_a_usuario(self, usuario):
        return usuario.libros_prestados