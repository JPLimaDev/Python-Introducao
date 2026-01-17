#Escreva um programa que receba notas de um aluno ( 0 - 10 ) , caso
# A nota digitada esteja fora desse intervalo peça para o professor digitar novamente

nota = float(input("Digite a nota do aluno (0-10):"))

while nota < 0 or nota > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota = float(input("Digite a nota do aluno (0-10):"))
   
print(f"A nota válida do aluno é: {nota:.2f}")
