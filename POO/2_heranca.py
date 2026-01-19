class Pessoa:

    def andar(self):
        print("Andando...")

    def falar(self):
        print("Falando...")

class Cliente(Pessoa):
    def comprar(self):
        print("Comprando...")



class Vendendor(Pessoa):
    def vender(self):
        print("Vendendo...")

c1 = Cliente()

c1.comprar()

