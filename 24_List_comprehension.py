#List_comprehension usa-se para criar listas de forma concisa e eficiente.

'''x = [ [input('Digite um numero:') for j in range(4, 7)] for i in range(0,3)] #Cria uma lista com 3 listas internas, cada uma contendo os números de 4 a 6.



print(x)'''

x = [i for i in range(10) if i > 4]#Cria uma lista com números de 0 a 9, mas apenas os maiores que 4.

print(x)