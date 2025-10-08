import threading
import queue

# Patron de diseño: Objeto Activo :
# Permite que las funciones del programa se ejecuten de manera asíncrona para manejar múltiples tareas concurrentes sin bloquear el flujo principal.
# Se decidio utilizar debido a que se requieren manejar múltiples pedidos de manera concurrente, permitiendo que varios cocineros (hilos) preparen pedidos al mismo tiempo sin bloquearse entre sí.
# Primero se encolan los pedidos y luego cada cocinero va preparando los pedidos de manera independiente y la cola se va vaciando.

#Servicio que gestiona cocineros (objetos activos) y cola de pedidos.
class ServicioPedidos:
    def __init__(self, num_cocineros=2):  #constructor recibe número de cocineros
        #cola thread-safe
        self.cola_pedidos = queue.Queue()
        self.cocineros = []
        self.activo = True

        # Crear hilos cocineros (Objetos Activos)
        for i in range(num_cocineros): #cada cocinero va a ser un hilo
            cocinero = threading.Thread( #se crea un hilo
                target=self._worker, #función
                args=(i + 1,), #id
                daemon=True #cierre
            )
            self.cocineros.append(cocinero) #agrega el hilo a la lista de cocineros

    def _worker(self, id_cocinero): #función que ejecuta cada cocinero
        while self.activo:
            try:
                pedido = self.cola_pedidos.get(timeout=1) #toma un pedido de la cola
                #procesar el pedido
                print(f"[COCINERO {id_cocinero}] Preparando {pedido}")
                resultado = pedido.preparar()
                print(f"[COCINERO {id_cocinero}] {resultado}")
                self.cola_pedidos.task_done()
            except queue.Empty:
                continue

    def agregar_pedido(self, pedido):
        self.cola_pedidos.put(pedido)

    def iniciar_servicio(self):
        for cocinero in self.cocineros:
            cocinero.start()
        #print(f"[SISTEMA] {len(self.cocineros)} cocineros iniciados")

    def procesar_pedidos(self):
        self.iniciar_servicio()
        self.cola_pedidos.join()
        #print("[SISTEMA] Todos los pedidos procesados")

    def detener_servicio(self):
        self.activo = False
        print("[SISTEMA] Servicio de pedidos terminado.")
