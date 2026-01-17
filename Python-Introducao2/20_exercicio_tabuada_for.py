#Receba um numero e mostra a tabuada completa dele usando o laço for

num_digitado = int(input('Digite um numero para ver a tabuada completa: '))

for i in range(0, 11):
    print(f'{num_digitado} x {i} = {num_digitado * i}')