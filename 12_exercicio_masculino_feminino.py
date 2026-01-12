#Receba F para feminino e M para masculino e exiba a mensagem "Feminino" ou "Masculino"

sexo = input('Digite F para feminino e M para masculino:').strip().upper()

if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
else:
    print('Sexo inválido')