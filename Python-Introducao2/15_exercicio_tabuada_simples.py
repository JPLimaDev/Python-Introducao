#Receba um número inteiro do usuário e imprima a tabuada desse número

num = int(input("Digite um número inteiro para ver a tabuada: "))

print(f"Tabuada do {num}:")

i = 0
while i <= 10:
    result = num * i
    print(f"{num} x {i} = {result}")    
    i += 1
