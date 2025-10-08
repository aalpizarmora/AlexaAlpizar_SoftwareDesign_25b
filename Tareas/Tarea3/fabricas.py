from abc import ABC, abstractmethod
from pedidos import Hamburguesa, Pizza

#Clase abstracta para crear pedidos.
class CreadorPedidos(ABC):
    @abstractmethod
    def crear_pedido(self, id):
        pass

#Crea pedidos de tipo Hamburguesa
class CreadorHamburguesas(CreadorPedidos):
    def crear_pedido(self, id):
        return Hamburguesa(id)

#Crea pedidos de tipo Pizza
class CreadorPizzas(CreadorPedidos):
    def crear_pedido(self, id):
        return Pizza(id)
