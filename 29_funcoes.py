#Funções
#Como usar funções em Python
#Criar, chamar, parâmetros, retorno
'''
#Criar uma função
def minha_funcao():
    print("Olá, mundo!")'

#Chamar a função
minha_funcao()

#Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Alice")

#Função com retorno
def soma(a, b):
    return a + b
resultado = soma(3, 5)
print(resultado)
'''

#Função que contem 2 parâmetros e retorna a soma deles
#args - Argumentos variáveis (números indefinidos de parâmetros)
#kwargs - Argumentos nomeados variáveis (números indefinidos de parâmetros nomeados)
'''def soma_numeros(**kwargs):
    x = kwargs.get('teste4')
    if x:
        print('Foi passado o teste4')
    else:
        print('Não foi passado o teste4')
    print(x)

soma_numeros(teste1 = 10 , teste2 = 20, teste3 = 30 )'''

def soma_valores(n1 , n2):
    soma = n1 + n2
    return soma

y = soma_valores(1, 2)
print(y)