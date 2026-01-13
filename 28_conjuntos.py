#Conjuntos
#Como usar conjuntos em Python
#Não pode ter elementos repetidos
#Union, interseção, diferença

#Union
#Mostrar tudo sem repetição
'''x = {1, 2, 3 ,4 ,5}
y = {6, 7, 8,  9, 10}

t = x.union(y)
print(t)'''

#Intersecção
#Mostrar tudo sem repetição

'''x = {1, 2, 3 ,4 ,5}
y = {4, 5, 6, 7, 8}

t = x.intersection(y)
print(t)'''

#Diferença
#Mostrar o que tem em x que não tem em y
'''x = {1, 2, 3 ,4 ,5}
y = {4, 5, 6, 7, 8}
t = x.difference(y)
print(t)'''

#Symetric Difference
#Mostrar o que tem em x e y, mas não em ambos
x = {1, 2, 3 ,4 ,5}
y = {4, 5, 6, 7, 8}
t = x.symmetric_difference(y)
print(t)