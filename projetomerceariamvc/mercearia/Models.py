from datetime import datetime
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
        

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, quantidade_Vendida, data = datetime.now()):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_Vendida = quantidade_Vendida
        self.data = data


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa: #Classe cliente 
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa): #Herança simples de pessoa que no caso é cliente e funcionario herda os atributos
    def __init__(self, clt, nome, email, telefone):
        super().__init__(nome, email, telefone)
        self.clt = clt