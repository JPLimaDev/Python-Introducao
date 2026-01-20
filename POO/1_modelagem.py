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

    @classmethod #Methodo de classe
    def andar(cls):
        cls.pernas = 2
        return None
    
    @staticmethod
    def e_adulto(idade):
        if idade >= 18:
            return True
        return False


# print(Pessoas.possui_boca) 

# p1 = Pessoas('João', 25)

# p1.andar()

print(Pessoas.e_adulto(21))