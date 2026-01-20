#Interface grafica View
from controller import PessoaController
while True:
    decisao = int(input('Digite 1 para salvar uma pessoa ou digite 2 para ver a pessoa salva e 3 para sair:'))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite o nome:')
        idade = int(input('Digite a idade:'))
        cpf = input('Digite o cpf:')
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Pessoa cadastrada com sucesso:')
        else:
            print('Erro ao cadastrar pessoa, Digite os dados corretamente')

