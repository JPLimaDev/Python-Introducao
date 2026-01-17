#Tratamentos de Exceções
#try, except, finally, raise
'''
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
try:
    print(n1/n2)
except ZeroDivisionError as e:
    print("Não é possível dividir por zero!")
    print(e)

finally:
    print("Operação finalizada.")'''

#Exemplo de tratamento de múltiplas exceções
'''try: 
    x = int(input("Digite um número: "))

    print(5/x)
except ValueError:
    print("Valor inválido! Digite um número inteiro.")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
finally:
    print("Fim do programa.")'''

try:
    x = int(input("Digite um número: "))
    print(5/x)
except Exception as e:
    print(e)