from fabricas import CreadorHamburguesas, CreadorPizzas
from ServicioPedidos import ServicioPedidos
from lotes import crear_lotes_pedidos

if __name__ == "__main__":
    #crear servicio con 2 cocineros (objetos activos)
    servicio = ServicioPedidos(num_cocineros=2)

    #factories
    fabrica_h = CreadorHamburguesas()
    fabrica_p = CreadorPizzas()

    #cantidad de pedidos
    print("--CREANDO PEDIDOS--")
    hamburguesas = crear_lotes_pedidos(fabrica_h, 3, 0)
    pizzas = crear_lotes_pedidos(fabrica_p, 2, 3)

    #agrega todos los pedidos al servicio
    todos = hamburguesas + pizzas

    for pedido in todos:
        servicio.agregar_pedido(pedido) #se agrega al servicio
        print(f"[SISTEMA] Pedido {pedido.id} en cola")

    #procesar todos los pedidos
    print(f"\n--PROCESANDO {len(todos)} PEDIDOS--")
    servicio.procesar_pedidos()
    servicio.detener_servicio()
