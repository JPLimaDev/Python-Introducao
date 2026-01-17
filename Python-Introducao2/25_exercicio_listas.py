#Receba 10 valores e exiba a soma de todos eles

valores = []

for i in range(10):
    valor = int(input(f'Informar o {i+1}º valor: '))
    valores.append(valor)
    for j in range(valores[i]):
        print(j)
