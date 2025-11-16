class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.listo = False

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def marcar_listo(self):
        self.listo = True
        print(f"[Sistema]: Pedido listo para {self.cliente.nombre}")