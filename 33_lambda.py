#Funções lambda são funções anonimas na qual funcionam de forma eficiente quando se trata de realizar 
#tarefas rapidas, curtas.

#Comando para utilizar essa função dentro de outras funções, lambda argumentos: expressão
'''def teste():
    return lambda *idade: print(idade)

x = teste()
x('caio', 'joao')'''

'''
#Filter
x = [{'nome': 'joao', 'idade': 22}, {'nome': 'marcos', 'idade': 40}]

x = list(filter(lambda x: x['idade'] >= 22 , x))
print(x)'''

#Map Faz uma interação na lista e transforma eles
x = [{'nome': 'joao', 'idade': 20}, {'nome': 'lukas', 'idade': 40}]

x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor que 30 anos'} if x['idade'] < 39 else(x) , x))

print(x)