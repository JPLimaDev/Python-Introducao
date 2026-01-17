#Faça um programa que o usuario possa cadastrar n pessoas
#Armazenando seu nome, idade, altura

pessoas = []


pessoa = input("Deseja cadastrar uma nova pessoa? (s/n) ")

while pessoa == 's':
    nome = input("Digite o nome:")
    idade = int(input("Digite a idade:"))
    altura = float(input("Digite a altura:"))

    pessoas.append({'nome': nome, 'idade': idade, 'altura': altura})
    pessoa = input("Deseja cadastrar uma nova pessoa? (s/n) ")
    
print("Pessoas cadastradas:")
for p in pessoas:
    print(f"Nome: {p['nome']}, Idade: {p['idade']}, Altura: {p['altura']}")
