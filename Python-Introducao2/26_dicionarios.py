#Dicionarios em python
#Dicionarios sao estruturas de dados que armazenam pares de chave-valor
#len(dicionario) - Retorna o numero de itens no dicionario
#dicionario[chave] = valor - Adiciona ou atualiza o valor associado a uma chave
#del dicionario[chave] - Remove o item com a chave especificada
#dicionario.keys() - Retorna uma lista de todas as chaves no dicionario
#dicionario.values() - Retorna uma lista de todos os valores no dicionario
#dicionario.items() - Retorna uma lista de tuplas contendo pares chave-valor
#dicionario.get(chave, valor_padrao) - Retorna o valor associado a 
#chave ou valor_padrao se a chave nao existir
#dicionario.clear() - Remove todos os itens do dicionario
#dicionario.copy() - Retorna uma copia rasa do dicionario
#dicionario.update(outro_dicionario) - Atualiza o dicionario com os pares chave-valor de outro_dicionario

pessoa = {
    'nome': 'Joao',
    'idade': 25,
    'altura': 1.75}  

print(pessoa.values())  # Retorna todos os valores do dicionario
print(pessoa.keys())    # Retorna todas as chaves do dicionario
print(pessoa.items())   # Retorna todos os itens (pares chave-valor) do dicionario
