from abc import ABC, abstractmethod
import time, random

#Clase base abstracta para cualquier tipo de pedido.
class Pedido(ABC):
    def __init__(self, id):
        self.id = id
        self.tipo = ""

    @abstractmethod
    def preparar(self):
        pass

    def __str__(self):
        return f"{self.tipo} {self.id}"

#Clase para pedidos de tipo Hamburguesa
class Hamburguesa(Pedido):
    def __init__(self, id):
        super().__init__(id)
        self.tipo = "Hamburguesa"

    def preparar(self):
        time.sleep(random.uniform(1, 3)) #simula tiempo de preparación
        return f"Hamburguesa {self.id} preparada"

#Clase para pedidos de tipo Pizza
class Pizza(Pedido):
    def __init__(self, id):
        super().__init__(id)
        self.tipo = "Pizza"

    def preparar(self):
        time.sleep(random.uniform(2, 4))
        return f"Pizza {self.id} preparada"
