class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = "Ser Humano"
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade


    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retorna_nome()} está logando no sistema')

print(Pessoas.possui_boca) 