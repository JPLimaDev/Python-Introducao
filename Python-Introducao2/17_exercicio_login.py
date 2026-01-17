#Defina um usuario e senha e depois verifique se o login do usuario é valido

usuario_correto = "admin"
senha_correta = "senha123"

usuario = input("Digite o nome de usuario:")
senha = input("Digite a senha:")

while usuario != usuario_correto or senha != senha_correta:
    print("Usuario ou senha incorretos! Tente novamente.")
    usuario = input("Digite o nome de usuario:")
    senha = input("Digite a senha:")

print("Login realizado com sucesso!")