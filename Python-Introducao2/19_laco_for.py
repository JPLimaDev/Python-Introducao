#Entendendo laços de repetição for
#No laço for, o ultimo valor não é incluso, por exemplo:
#for i in range(0, 10): #Vai de 0 até 9
#Usa-se for quando se sabe o número exato de repetições

#For aninhado (laço dentro de outro laço)
for i in range(0, 3): #Laço externo
    for j in range(0, 2): #Laço interno
       #Fica nesse laço interno até terminar o laço interno
        print(f'Fim do laço interno externo {i} interno {j}') #Depois que termina o laço interno, volta para o laço externo
