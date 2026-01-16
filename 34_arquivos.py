#Arquivos

arquivo = open('pessoas.txt', 'r') #open ('arquivo', 'metodos de leitura') w - escrita, a - append, r - leitura
#Write Escreve dentro do arquivo, só que se colocar outro e rodar novamente ele substitui o que estava 
#Append Adiciona no arquivo o texto inserido sem apagar o que tinha
#Read Ler arquivos usando read() - retorna char, readlines() - nome inteiro
'''i = 0
while True:
    if i > 1:
        break
    arquivo.write(input('Digite o nome da pessoa:') + " " + input('Digite a sua idade:') + '\n')
    i +=1'''
'''
result = arquivo.readlines()
x = []
for i in result:
    x.append(i.split())

print(x[1][1])

arquivo.close()'''
#Utiliza with open para abrir o arquivo e fechar automaticamente.
with open('pessoas.txt', 'r') as arq:
    x = arq.read()
    print(x)