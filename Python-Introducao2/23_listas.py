#Usando listas com Python
#Usa-se lista para armazenar varios valores em uma unica variavel entao manipula-los depois
#len(lista) - Retorna o tamanho da lista
#lista.append(valor) - Adiciona um valor ao final da lista
#lista.insert(indice, valor) - Adiciona um valor em um indice especifico
#lista.pop() - Remove o ultimo valor da lista
#lista.pop(indice) - Remove o valor do indice especifico
#lista.remove(valor) - Remove o valor especifico
#lista.sort() - Ordena a lista em ordem crescente
#sorted(lista) - Retorna uma nova lista ordenada sem alterar a original
#lista.reverse() - Inverte a ordem da lista
#enumerate(lista) - Retorna o indice e o valor de cada item da lista
#alterar valor de uma posicao especifica da lista fica assim: lista[indice] = novo_valor
#como encontra index de um valor especifico: lista.index(valor)

'''i = 0

idades = [
    [10, 20, 30],
    [25, 35, 45]   
]

for i in range(len(idades)):
    print(f'Idades do grupo {i+1}:')
    for idade in idades[i]:
        print(idade)'''

#id() - Retorna o endereco de memoria do objeto
#hex() - Converte um numero inteiro para hexadecimal
#copy() - Cria uma copia rasa da lista

x = [1, 2 , 3]
y = x.copy()
y[0] = 10

print(x)
print(y)
