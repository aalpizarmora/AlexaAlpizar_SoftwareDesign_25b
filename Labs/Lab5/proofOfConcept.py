from abc import ABC, abstractmethod
from typing import List

# Interfaz para estrategias de transporte
class TransportStrategy(ABC):
    @abstractmethod
    def calcular_tarifa(self) -> float:
        pass
    
    @abstractmethod
    def calcular_tiempo(self) -> float:
        pass

# Implementaciones concretas de transporte
class BusStrategy(TransportStrategy):
    def calcular_tarifa(self) -> float:
        return 800
    
    def calcular_tiempo(self) -> float:
        return 30

class TrenStrategy(TransportStrategy):
    def calcular_tarifa(self) -> float:
        return 1200
    
    def calcular_tiempo(self) -> float:
        return 20

class FerryStrategy(TransportStrategy):
    def calcular_tarifa(self) -> float:
        return 1500
    
    def calcular_tiempo(self) -> float:
        return 45

# Decorator base para descuentos
class DescuentoDecorator(ABC):
    def __init__(self, tarifa_base: float):
        self._tarifa_base = tarifa_base
    
    @abstractmethod
    def aplicar_descuento(self) -> float:
        pass

# Decorators concretos para diferentes descuentos
class DescuentoEstudiante(DescuentoDecorator):
    def aplicar_descuento(self) -> float:
        return self._tarifa_base * 0.95  # -5%

class DescuentoAdultoMayor(DescuentoDecorator):
    def aplicar_descuento(self) -> float:
        return self._tarifa_base * 0.85  # -15%

# Clase principal del sistema
class SistemaTransporte:
    def __init__(self):
        self.transportes: List[TransportStrategy] = []
    
    def agregar_transporte(self, transporte: TransportStrategy):
        self.transportes.append(transporte)
    
    def calcular_viaje_combinado(self, descuentos: List[str] = None) -> float:
        if descuentos is None:
            descuentos = []
        
        tarifa_base = sum(transporte.calcular_tarifa() for transporte in self.transportes)
        tiempo_total = sum(transporte.calcular_tiempo() for transporte in self.transportes)
        
        # Mostrar detalles del viaje
        nombres_transportes = [type(t).__name__.replace('Strategy', '') for t in self.transportes]
        print(f"Calculando viaje combinado: {' + '.join(nombres_transportes)}")
        print(f"Tarifa base total: {tarifa_base} colones")
        print(f"Tiempo total estimado: {tiempo_total} minutos")
        
        # Aplicar descuentos dinámicamente
        tarifa_final = tarifa_base
        
        for descuento in descuentos:
            if descuento == "estudiante":
                tarifa_final = DescuentoEstudiante(tarifa_final).aplicar_descuento()
                print("Aplicando descuento de estudiante (-5%)")
            elif descuento == "adultoMayor":
                tarifa_final = DescuentoAdultoMayor(tarifa_final).aplicar_descuento()
                print("Aplicando descuento adulto mayor (-15%)")
        
        print(f"Tarifa final: {round(tarifa_final)} colones")
        print("-" * 50)
        return tarifa_final

# Ejemplo de uso
if __name__ == "__main__":
    sistema = SistemaTransporte()
    
    # Viaje: Bus + Tren
    sistema.agregar_transporte(BusStrategy())
    sistema.agregar_transporte(TrenStrategy())
    sistema.calcular_viaje_combinado(["estudiante"])
    
    # Viaje solo con Bus y descuento adulto mayor
    sistema2 = SistemaTransporte()
    sistema2.agregar_transporte(BusStrategy())
    sistema2.calcular_viaje_combinado(["adultoMayor"])