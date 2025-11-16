from abc import ABC, abstractmethod

# clase base
class Producto(ABC):
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def costo(self):
        pass

# productos concretos
class Bebida(Producto):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def descripcion(self):
        return self.nombre

    def costo(self):
        return self.precio

class Alimento(Producto):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def descripcion(self):
        return self.nombre

    def costo(self):
        return self.precio

# decoradores
class Decorador(Producto):
    def __init__(self, producto):
        self.producto = producto

    def descripcion(self):
        return self.producto.descripcion()

    def costo(self):
        return self.producto.costo()

class ConLeche(Decorador):
    def descripcion(self):
        return self.producto.descripcion() + " con leche"

    def costo(self):
        return self.producto.costo() + 0.5

class ConCanela(Decorador):
    def descripcion(self):
        return self.producto.descripcion() + " y canela"

    def costo(self):
        return self.producto.costo() + 0.3

class ConRelleno(Decorador):
    def __init__(self, producto, tipo):
        super().__init__(producto)
        self.tipo = tipo

    def descripcion(self):
        return self.producto.descripcion() + f" con relleno de {self.tipo}"

    def costo(self):
        return self.producto.costo() + 1.0