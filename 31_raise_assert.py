#Raise e asserts
#Raise - Lançar exceções personalizadas
#Asserts - Verificações durante o desenvolvimento

#Raise
'''def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("Os números devem ser maiores ou iguais a zero.")
    return n1 + n2

#Asserts 
print(soma(2, 2))'''
x = -2
assert x > 0, "x deve ser maior que zero"
print(x)