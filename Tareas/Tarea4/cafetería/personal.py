class Barista:
    def preparar_bebida(self, bebida):
        print(f"[Barista]: Preparo bebida: {bebida.descripcion()}")

class Pastelero:
    def preparar_alimento(self, alimento):
        print(f"[Pastelero]: Preparo alimento: {alimento.descripcion()}")

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre