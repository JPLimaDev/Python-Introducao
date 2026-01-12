#Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6)
#Se ele ficou de recuperacao (nota maior ou igual a 4) ou se ele foi
# Reprovado (nota menor que 4). Mostre tambem a media do aluno.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print('Aprovado')
elif media >= 4 and media < 6:
    print('Recuperação')
else:
    print('Reprovado')

print(f'Média')