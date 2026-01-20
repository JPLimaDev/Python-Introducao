#Dao - Como os dados sao armazenados
from model import Pessoa
class PessoaDao:
    @classmethod #Metodo de classe, por que nao vai precisar de instancia
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arq: #Abre o arquivo no modo append e fecha
            arq.write(f'{pessoa.nome}, {pessoa.idade}, {pessoa.cpf}\n')

    @classmethod
    def ler(cls):
        nome = 'caio'
        idade = 19
        cpf = '123.456.789-10'
        return Pessoa(nome, idade, cpf)      
    

