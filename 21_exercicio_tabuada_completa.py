#Mostra a tabuada completa de todos os números entre 1 e 10 usando o laço for

for i in range(0, 11):
    print(f'\nTabuada do {i}:')
    for j in range(0, 11):
        print(f'{i} x {j} = {i * j}')