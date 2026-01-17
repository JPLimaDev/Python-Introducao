#Receba um numero e mostre todos os numero pares de 0 até o numero digitado

numero_digitado_usuario = int(input("Digite um número inteiro positivo: "))
i = 0

while i <= numero_digitado_usuario:
    if i % 2 == 0:
        print(i)
    i += 1