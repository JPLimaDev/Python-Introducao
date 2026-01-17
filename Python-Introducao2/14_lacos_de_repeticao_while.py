#Laço de repetição while

'''
i = 0 
j = 0
while i < 10 and j < 30 : #Usa-se while quando não souber o número exato de repetições
    print('Executa enquanto a condição for verdadeira')
    print('ola tudo bem?')
    i = i + 1  # Incrementa o valor de i para evitar loop infinito
    j = j + 10 '''
'''
i = 0

while i < 10:
    print(i)
    if i == 5: 
        break  # Interrompe o laço quando i for igual a 5
    i += 1'''

i = 0
while i < 10:
    print(i)
    if i % 2 == 1:
        i += 2  # Incrementa o valor de i para evitar loop infinito
        continue # Pula para a próxima iteração do laço e nunca incrementa o valor de i
    i += 1  # Incrementa o valor de i para evitar loop infinito