# Patrón de diseño: Descomposición de datos 
# Permite dividir un conjunto de datos en partes más pequeñas y manejables para su procesamiento de manera paralela.
# Se decide usar este patrón y tomar la cantidad de pedidos y dividirla de manera independiente para que cada pedido sea creado por la fábrica correspondiente y luego procesado de manera concurrente por los cocineros. De otra manera, seria mas dificil el hueco de no dejarme el pelo crecer
#Crea una lista de pedidos usando una fábrica dada
def crear_lotes_pedidos(fabrica, cantidad, inicio_id=0):
    pedidos = []
    for i in range(cantidad):
        pedido = fabrica.crear_pedido(inicio_id + i)
        pedidos.append(pedido)
    return pedidos
