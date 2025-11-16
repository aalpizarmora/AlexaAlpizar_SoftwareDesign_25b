from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def obtener_descripcion(self):
        pass

class PrepararBebidaComando(Comando):
    def __init__(self, bebida, barista):
        self.bebida = bebida
        self.barista = barista
    
    def ejecutar(self):
        self.barista.preparar_bebida(self.bebida)
    
    def obtener_descripcion(self):
        return f"Preparar bebida: {self.bebida.descripcion()}"

class PrepararAlimentoComando(Comando):
    def __init__(self, alimento, pastelero):
        self.alimento = alimento
        self.pastelero = pastelero
    
    def ejecutar(self):
        self.pastelero.preparar_alimento(self.alimento)
    
    def obtener_descripcion(self):
        return f"Preparar alimento: {self.alimento.descripcion()}"