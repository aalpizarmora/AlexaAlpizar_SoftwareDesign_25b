from producto import Bebida, Alimento, ConLeche, ConCanela, ConRelleno
from personal import Cliente
from pedido import Pedido
from sistema import SistemaCafeteria

class Main:
    def __init__(self):
        self.sistema = SistemaCafeteria()
    
    def crear_pedido_ana(self):
        """Crea y retorna el pedido de Ana"""
        ana = Cliente("Ana")
        pedido = Pedido(ana)
        
        cafe = Bebida("Cafe", 2.0)
        cafe_personalizado = ConCanela(ConLeche(cafe))
        
        croissant = Alimento("Croissant", 1.5)
        croissant_personalizado = ConRelleno(croissant, "chocolate")
        
        pedido.agregar_producto(cafe_personalizado)
        pedido.agregar_producto(croissant_personalizado)
        
        return pedido
    
    def crear_pedido_carlos(self):
        """Crea y retorna el pedido de Carlos"""
        carlos = Cliente("Carlos")
        pedido = Pedido(carlos)
        
        te = Bebida("Te verde", 1.8)
        espresso = Bebida("Cafe doble espresso", 2.5)
        espresso_con_crema = ConLeche(espresso)
        
        pedido.agregar_producto(te)
        pedido.agregar_producto(espresso_con_crema)
        
        return pedido
    
    def ejecutar(self):
        """Método principal que ejecuta toda la simulación"""
        print("=== SIMULACIÓN DE CAFETERÍA ===\n")
        
        # Crear pedidos
        pedido_ana = self.crear_pedido_ana()
        pedido_carlos = self.crear_pedido_carlos()
        
        # Procesar pedidos
        self.sistema.procesar_pedido(pedido_ana)
        self.sistema.procesar_pedido(pedido_carlos)
        
        print("\n=== TODOS LOS PEDIDOS PROCESADOS ===")
        
        # Mostrar resumen de costos
        self.mostrar_resumen(pedido_ana, pedido_carlos)
    
    def mostrar_resumen(self, pedido_ana, pedido_carlos):
        """Muestra un resumen de los costos de los pedidos"""
        print("\n--- RESUMEN DE COSTOS ---")
        
        costo_ana = sum(producto.costo() for producto in pedido_ana.productos)
        costo_carlos = sum(producto.costo() for producto in pedido_carlos.productos)
        
        print(f"Pedido de Ana: ${costo_ana:.2f}")
        for producto in pedido_ana.productos:
            print(f"  - {producto.descripcion()}: ${producto.costo():.2f}")
        
        print(f"\nPedido de Carlos: ${costo_carlos:.2f}")
        for producto in pedido_carlos.productos:
            print(f"  - {producto.descripcion()}: ${producto.costo():.2f}")
        
        print(f"\nTOTAL: ${costo_ana + costo_carlos:.2f}")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = Main()
    app.ejecutar()