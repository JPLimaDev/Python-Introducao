
#Sobreposição de metodos
#A classe filha sempre tem prioridade sobre a classe mãe a não ser que usemos o super()

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf):
        self.id_cliente = id_cliente
        super().__init__(nome, cpf)

class Vendendor(Pessoa):
    def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

c1 = Cliente(2, 'Caio', '123.123.123-12')
v1 = Vendendor(3, 'Ana', '321.321.321-32')

print(c1.id_cliente)
print(v1.nome)
print(v1.cpf)
