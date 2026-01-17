#Geradores
#Função geradora 
from pympler.asizeof import asizesof

def dobro(lista):
    for i in lista:
        yield i

x = dobro(range(0,))





