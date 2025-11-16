from producto import Bebida, Alimento, ConLeche, ConCanela
from comando import PrepararBebidaComando, PrepararAlimentoComando
from personal import Barista, Pastelero

class SistemaCafeteria:
    def __init__(self):
        self.comandos_pendientes = []
        self.barista = Barista()
        self.pastelero = Pastelero()
    
    def procesar_pedido(self, pedido):
        print(f"\n--- Procesando pedido de {pedido.cliente.nombre} ---")
        
        # Crear comandos para cada producto
        for producto in pedido.productos:
            if isinstance(producto, Bebida) or any(isinstance(producto, cls) for cls in [ConLeche, ConCanela]):
                comando = PrepararBebidaComando(producto, self.barista)
            else:
                comando = PrepararAlimentoComando(producto, self.pastelero)
            
            self.comandos_pendientes.append(comando)
        
        # Ejecutar todos los comandos
        for comando in self.comandos_pendientes:
            print(f"[Sistema] → {comando.obtener_descripcion()}")
            comando.ejecutar()
        
        # Finalizar pedido
        pedido.marcar_listo()
        self.comandos_pendientes.clear()