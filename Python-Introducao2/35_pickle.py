import pickle
#Serialização de objeto, seria pegar algo que está em memória e torná-lo persistente
'''
x = {'nome': 'caio', 'idade': 20}
#Dumps recebe apenas o objeto retorna apenas a string binaria do
#arquivo serializado 
# e dump o objeto e arquivo (salvar)
#Loads desserializa o objeto ou dados

string = (pickle.dumps(x))

print(pickle.loads(string)['nome'])'''
#Para cada objeto dentro do arquivo serializado tem-se que realizar o load
class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
p1 = Pessoas('Marcos', 21)

x = [1,2,3,4]

arq = open('arquivo.pkl', 'wb') #Abriu o arquivo no modo escrita e inseriu dado em forma binaria
pickle.dump(p1, arq)#Serializou o objeto e colocou no arquivo

arq = open('arquivo.pkl', 'rb')#Abriu o arquivo em formato de leitura e desserializou
retornou = pickle.load(arq) #Desserializou
print(retornou.nome)
arq.close()