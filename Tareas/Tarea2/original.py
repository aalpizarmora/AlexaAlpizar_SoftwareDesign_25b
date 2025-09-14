class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    def calculator_popularidad(self):
        if self.genero == 'novela':
            base = 50
            extra = self.paginas / 10
        elif self.genero == 'ciencia':
            base = 70
            extra = self.paginas / 5
        elif self.genero == 'historia':
            base = 40
            extra = self.paginas / 8
        else:
            base = 10
            extra = 0
        return base + extra

    def es_antiguo(self):
        if self.anio_publicacion < 1980:
            return True
        else:
            return False

    def imprimir_datos(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.paginas}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Disponible: {'sí' if self.disponible else 'No'}")
        print(f"Popularidad: {self.calculator_popularidad()}")
        print(f"Es antiguo: {'sí' if self.es_antiguo() else 'No'}")
        print("---")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Género (novela/ciencia/historia): ").lower()
        paginas = int(input("Número de páginas: "))
        anio = int(input("Año de publicación: "))
        
        libro = Libro(titulo, autor, genero, paginas, anio)
        self.libros.append(libro)
        print("Libro agregado!")

    def generar_reporte(self):
        total = len(self.libros)
        antiguos = 0
        disponibles = 0
        popularidad_total = 0

        for libro in self.libros:
            libro.imprimir_datos()
            if libro.es_antiguo():
                antiguos += 1
            if libro.disponible:
                disponibles += 1
            popularidad_total += libro.calculator_popularidad()

        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {total}")
        print(f"Disponibles: {disponibles}")
        print(f"Antiguos: {antiguos}")
        print(f"Promedio de popularidad: {popularidad_total / total if total > 0 else 0}")