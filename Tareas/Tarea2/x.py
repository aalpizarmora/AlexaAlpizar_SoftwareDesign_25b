#  SRP: Single Responsability Principle
#  Libro realizaba muchas funciones, entonces se separan en otras clases.
#  Cada clase tiene una única responsabilidad. Hace una sola funcionalidad y favorece el mantenimiento.
class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

#   OCP: Open/Closed Principle
#   No se podían agregar nuevos géneros sin modificar el código existente.
#   Se usa estructura general para el cálculo de popularidad y agregar más.
from abc import ABC, abstractmethod

class PopularidadStrategy(ABC):
    @abstractmethod
    def calcular(self, libro: Libro) -> float:
        pass

class PopularidadNovelaStrategy(PopularidadStrategy):
    def calcular(self, libro: Libro) -> float:
        return 50 + (libro.paginas / 10)

class PopularidadCienciaStrategy(PopularidadStrategy):
    def calcular(self, libro: Libro) -> float:
        return 70 + (libro.paginas / 5)

class PopularidadHistoriaStrategy(PopularidadStrategy):
    def calcular(self, libro: Libro) -> float:
        return 40 + (libro.paginas / 8)

class PopularidadDefaultStrategy(PopularidadStrategy):
    def calcular(self, libro: Libro) -> float:
        return 10

class PopularidadService:
    def __init__(self):
        self.strategies = {
            'novela': PopularidadNovelaStrategy(),
            'ciencia': PopularidadCienciaStrategy(),
            'historia': PopularidadHistoriaStrategy()
        }
        self.default_strategy = PopularidadDefaultStrategy()
    
    def calcular_popularidad(self, libro: Libro) -> float:
        strategy = self.strategies.get(libro.genero, self.default_strategy)
        return strategy.calcular(libro)

# SRP: Single Responsability Principle
class AntiguedadService:
    @staticmethod
    def es_antiguo(libro: Libro) -> bool:
        return libro.anio_publicacion < 1980

# SRP
class LibroPresenter:
    def __init__(self, popularidad_service: PopularidadService, antiguedad_service: AntiguedadService):
        self.popularidad_service = popularidad_service
        self.antiguedad_service = antiguedad_service
    
    def presentar(self, libro: Libro):
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Género: {libro.genero}")
        print(f"Páginas: {libro.paginas}")
        print(f"Año: {libro.anio_publicacion}")
        print(f"Disponible: {'sí' if libro.disponible else 'No'}")
        print(f"Popularidad: {self.popularidad_service.calcular_popularidad(libro)}")
        print(f"Es antiguo: {'sí' if self.antiguedad_service.es_antiguo(libro) else 'No'}")
        print("---")

# ISP: Interface Segregation Principle
# La clase LibroRepository era una implementación concreta. Las clases que dependen de ella están acopladas a esta implementación específica.
# Se separa la interfaz y los clientes dependen de abstracciones.
class LibroRepository:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
    
    def obtener_todos(self) -> list[Libro]:
        return self.libros.copy()
    
    def contar_libros(self) -> int:
        return len(self.libros)

# SRP
class ReportService:
    def __init__(self, libro_repository: LibroRepository, popularidad_service: PopularidadService, 
                 antiguedad_service: AntiguedadService, libro_presenter: LibroPresenter):
        self.libro_repository = libro_repository
        self.popularidad_service = popularidad_service
        self.antiguedad_service = antiguedad_service
        self.libro_presenter = libro_presenter
    
    def generar_reporte(self):
        libros = self.libro_repository.obtener_todos()
        total = self.libro_repository.contar_libros()
        antiguos = 0
        disponibles = 0
        popularidad_total = 0

        for libro in libros:
            self.libro_presenter.presentar(libro)
            if self.antiguedad_service.es_antiguo(libro):
                antiguos += 1
            if libro.disponible:
                disponibles += 1
            popularidad_total += self.popularidad_service.calcular_popularidad(libro)

        print("\nREPORTE BIBLIOTECA:")
        print(f"Total libros: {total}")
        print(f"Disponibles: {disponibles}")
        print(f"Antiguos: {antiguos}")
        print(f"Promedio de popularidad: {popularidad_total / total if total > 0 else 0}")

# DIP: Dependency Inversion Principle
# Los módulos de alto nivel dependen de módulos de bajo nivel
# Ahora se pueden cambiar implementaciones sin afectar el servicio
class BibliotecaService:
    def __init__(self, libro_repository: LibroRepository):
        self.libro_repository = libro_repository
    
    def agregar_libro(self, libro: Libro):
        self.libro_repository.agregar_libro(libro)
        return libro

# SRP
class Biblioteca:
    def __init__(self, biblioteca_service: BibliotecaService, report_service: ReportService):
        self.biblioteca_service = biblioteca_service
        self.report_service = report_service
    
    def agregar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género (novela/ciencia/historia): ").lower()
        paginas = int(input("Número de páginas: "))
        anio = int(input("Año de publicación: "))
        
        libro = Libro(titulo, autor, genero, paginas, anio)
        self.biblioteca_service.agregar_libro(libro)
        print("Libro agregado!")
    
    def ejecutar(self):
        while True:
            print("\n1. Agregar libro")
            print("2. Generar reporte")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.report_service.generar_reporte()
            elif opcion == "3":
                break
            else:
                print("Opción no válida")

# DIP 
def main():
    libro_repository = LibroRepository()
    popularidad_service = PopularidadService()
    antiguedad_service = AntiguedadService()
    libro_presenter = LibroPresenter(popularidad_service, antiguedad_service)
    
    biblioteca_service = BibliotecaService(libro_repository)
    report_service = ReportService(libro_repository, popularidad_service, antiguedad_service, libro_presenter)
    
    ui = Biblioteca(biblioteca_service, report_service)
    ui.ejecutar()

if __name__ == "__main__":
    main()